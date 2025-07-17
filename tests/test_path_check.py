# tests/test_path_check.py
import pytest
import os
import sys

# scripts ディレクトリへのパスを Python のパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from verify_system_map_paths import verify_system_map_paths # スクリプトをインポート

pytest.importorskip("yaml") # yaml 未インストールで skip

def test_system_map_paths_are_valid():
    """
    system_map.yaml に記述されたファイルパスが全て存在するか検証する。
    """
    # system_map.yaml がプロジェクトのルートにあることを想定
    system_map_path = os.path.join(os.path.dirname(__file__), '..', 'system_map.yaml')

    # verify_system_map_paths 関数を実行し、結果をアサート
    # Falseが返された場合（エラーがあった場合）にテストを失敗させる
    assert verify_system_map_paths(system_map_path), "System map paths validation failed. Check console output for details."
