import os
import yaml
import pytest
from pathlib import Path
from typing import List, Optional, Union

# Pydanticを使ったデータモデルの定義
from pydantic import BaseModel, Field

# LangChainを使ったLLM連携
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage # これらのインポートはStrOutputParserを使うと通常不要だが、念のため残す
from langchain_core.output_parsers import StrOutputParser

# .envファイルから環境変数をロード
from dotenv import load_dotenv

load_dotenv()

# --- データモデル定義 ---
# PytestCollectionWarningを避けるため、テストクラスでないことを明示
# type: ignore
class ExpectedAnswer(BaseModel):
    contains_keywords: Optional[List[str]] = None
    exact_match: Optional[str] = None

# type: ignore
class TestCase(BaseModel):
    id: str
    name: str
    question: str
    context_files: List[str]
    expected_answer: ExpectedAnswer

# type: ignore
class TestSuite(BaseModel):
    test_suite: List[TestCase]

# --- テストデータ読み込み関数 ---
def load_test_suite() -> List[TestCase]:
    """ tests/regression/suite.yamlからテストケースを読み込む """
    suite_path = Path(__file__).parent / "regression" / "suite.yaml"
    if not suite_path.exists():
        pytest.fail(f"テストスイートファイルが見つかりません: {suite_path}")
    with open(suite_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return TestSuite(**data).test_suite

# --- Pytestのテスト関数 ---
@pytest.mark.parametrize("test_case", load_test_suite())
def test_os_regression(test_case: TestCase):
    """ Jibun OSの回帰テストを個別のテストケースについて実行する """
    
    # 1. コンテキストの構築
    project_root = Path(__file__).parent.parent
    context_str = ""
    for file_path in test_case.context_files:
        full_path = project_root / file_path
        if not full_path.exists():
            pytest.fail(f"コンテキストファイルが見つかりません: {file_path}")
        context_str += f"--- START OF FILE: {file_path} ---\n"
        context_str += full_path.read_text(encoding='utf-8')
        context_str += f"\n--- END OF FILE: {file_path} ---\n\n"
            
    # 2. LLMチェーンの準備
    if "GEMINI_API_KEY" not in os.environ:
        pytest.skip("GEMINI_API_KEYが設定されていません。")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite-preview-06-17", # 安定性の高いモデルを使用することを推奨
        temperature=0,
        google_api_key=os.environ.get("GEMINI_API_KEY")
    )
    
    # LangChain Expression Language (LCEL) を使用
    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "あなたは、提供されたコンテキスト情報のみに基づいて、ユーザーの質問に正確に答えるAIアシスタントです。"
            "コンテキストにない情報は「分かりません」と答えてください。"
            "回答は簡潔かつ明確に、関連するキーワードを含めてください。"
            "\n\n# コンテキスト\n{context}"
        ),
        HumanMessagePromptTemplate.from_template(
            "# 質問\n{question}"
        )
    ])
    
    # PromptTemplate | LLM | OutputParser でチェーンを構築
    # StrOutputParser を追加することで、LLMから直接文字列応答を得る
    chain = prompt_template | llm | StrOutputParser()
    
    # 3. AIに質問を実行
    try:
        # StrOutputParserが文字列を返すため、直接.strip()を適用
        ai_answer = chain.invoke({
            "context": context_str,
            "question": test_case.question
        }).strip()
    except Exception as e:
        pytest.fail(f"AIの質問実行中にエラーが発生しました: {e} for test_case.id={test_case.id}")

    print(f"\n--- Test Case: {test_case.id} ---")
    print(f"Question: {test_case.question}")
    print(f"AI Answer: {ai_answer}")
    
    # 4. 回答の検証 (アサーション)
    assert ai_answer, f"AIからの回答が空です: {test_case.id}"

    if test_case.expected_answer.contains_keywords:
        # 期待するキーワードリストの「いずれかの」キーワードが含まれていればパス
        found_any_keyword = False
        for keyword in test_case.expected_answer.contains_keywords:
            if keyword in ai_answer:
                found_any_keyword = True
                break # 一つでも見つかればループを抜ける
        
        # いずれのキーワードも見つからなかった場合にアサーションを失敗させる
        assert found_any_keyword, \
            f"回答に期待するキーワードのいずれも含まれていません。\n" \
            f"期待するキーワード: {test_case.expected_answer.contains_keywords}\n" \
            f"AIの回答: '{ai_answer}' for test_case.id={test_case.id}"

    if test_case.expected_answer.exact_match:
        assert test_case.expected_answer.exact_match == ai_answer, \
            f"回答が期待値と完全に一致しません: {test_case.id}"

