
## 🆕 デジタルツインOS - 「自己進化する知的生命システムの設計原理」ミニパック

v2025-07-14 r3 （四階層モデル / Digital Twin OS / バックログ統合対応）

> **このメモ＋下記 7 ファイル** を新チャットに貼れば、初見の AI でも同じ状況に復元し
> “Stateless 儀式” で **デジタルツインOSプラットフォーム** / **書籍執筆プロジェクト** ─ さらに **継続ドメイン** まで扱えます。

---

### 1️⃣ プロジェクト識別 & 現在地

| key            | value                          |
| -------------- | ------------------------------ |
| project\_id    | **os\_platform\_v1** |
| branch         | `feat/four-layer-fs-restructure` | # 最新のブランチ名に更新
| latest\_tag    | `v10.0.0-alpha.0` (PoC-1 DONE) |
| current\_stage | **1 / 5** — 基盤整備               |
| purpose\_short | *AI＋外部FBを高速循環し「学習データ→価値」を即転換* |

---

### 2️⃣ デジタルツインOSの四階層モデルによるディレクトリ構造（普遍 / 個人 それぞれにコンテンツ）

```

repo-root/
├─ constitution/            \# 憲法・魂 (L1)
│   ├─ common/
│   │   └─ constitution.yaml \# OSフレームワークの最高規範（普遍的憲法）
│   └─ personal/
│       └─ constitution.yaml \# あなた個人の憲法（究極の目的と価値観）
│
├─ legislation/             \# 法律・知恵 (L2)
│   ├─ common/
│   │   ├─ immune\_system.yaml        \# 知的免疫システムの普遍的フレームワーク
│   │   ├─ innate\_immunity.yaml      \# 普遍的なガードルール
│   │   ├─ mappings.yaml             \# 原則とガード等の関連性定義
│   │   ├─ implementation\_framework.yaml \# 実装ガイドの各フレームワーク定義
│   │   ├─ taxonomy.yaml             \# OS全体で共有されるタグや分類
│   │   ├─ prompt\_patterns.yaml      \# (計画中) 標準化されたプロンプトの型
│   │   ├─ projects/
│   │   │   └─ project\_template.yaml \# 普遍的なプロジェクトテンプレート
│   │   └─ domains/
│   │       └─ domain\_template.yaml  \# 普遍的なドメインテンプレート
│   └─ personal/
│       ├─ core\_principles.yaml \# 個人的な実装設定、役割、バックログなど
│       ├─ acquired\_immunity.yaml \# 個人的な獲得免疫ルール
│       ├─ profile.yaml             \# あなたの固定的なプロフィール
│       ├─ projects/
│       │    ├─ os\_platform.yaml     \# このデジタルツインOS開発プロジェクトの定義
│       │    └─ book\_writing.yaml    \# 書籍執筆プロジェクトの定義
│       └─ domains/
│            └─ learning.yaml        \# あなたの学習領域に関する定義
│
├─ precedents/              \# 判例・意識 (L3)
│   \# (現在、ファイルなし。将来的に記録から抽出されたパターンを配置)
│
├─ records/                 \# 記録・経験 (L4)
│   ├─ task\_log.yaml        \# タスクの進捗ログ
│   ├─ decision\_log.yaml    \# 意思決定の記録
│   └─ guard\_log.yaml       \# ガードの発動記録
│
├─ docs/                    \# ドキュメント
│   ├─ architecture\_overview.md
│   └─ charter.md
│
├─ .github/                 \# CI/CD関連
│   └─ workflows/
│       └─ validate.yaml
│
├─ system\_map.yaml          \# デジタルツインOS全体のファイル構造と役割を定義するマップ
└─ ... (その他の設定ファイル: .gitignore, README.md, requirements.txt など)

````

---

### 3️⃣ **constitution/common/constitution.yaml** – 初期内容（“普遍部分”のみ）

```yaml
---
version: "10.0.0"
last_updated: "2025-07-14" # 日付を更新

constitution:
  supreme_purpose: >
    本OSは「コピー可能な自己」を構築し、
    AI と協働しながら主体的・倫理的に進化するための
    不変の原則を提供する。

core_code:
  - name: "How→Why 抽出アプローチ"
  - name: "実践的効果重視"
  - name: "誠実性と透明性"

guards: # これは古い記述です。immune_system.yamlとinnate_immunity.yamlを参照するように変更
  - id: "G001"    # 構造化ガード
  - id: "G002"    # 計画的完了ガード
  - id: "G006"    # Value-Engineering Guard
  - id: "G008"    # セキュリティ & レジリエンス
````

*個人バイアス監視 (G005 等) や Traceability 原則は **legislation/personal/core\_principles.yaml** 側で override します。*

-----

### 4️⃣ **legislation/common/projects/project\_template.yaml**

```yaml
---
template_name: "general_project"
fields:
  project_id        : "<project_id>"
  purpose_short     : "<one-line purpose>"
  stakeholders      : []
  milestones        : []
  risks             : []
  default_tags      : ["obs","speed","value","security"]
```

### **legislation/common/domains/domain\_template.yaml**

```yaml
---
domain_id     : "<domain_id>"
purpose_short : "<continuous responsibility area>"
kpis: []
habits: []
default_tags  : ["obs","value","security"]
```

-----

### 5️⃣ Stateless “セッション儀式” (読み込み順更新済み)

| Step | トリガー                 | AI が読む順序                                                                                                                 | 出力       |
| ---- | -------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------- |
| 0    | **Human**: “作業を始めます” | ① `legislation/personal/profile.yaml` → ② `legislation/personal/core_principles.yaml` → ③ `legislation/common/taxonomy.yaml` → ④ `constitution/personal/constitution.yaml` → ⑤ 選択 project → (任意) 指定 domain | —        | \# 読み込み順序とパスを更新
| 1    | (自動) ブリーフィング         | todo 一覧 / Decision 要約 / 推奨タスク                                                                                            | Markdown |
| 2-4  | 選択→ドラフト→承認           | —                                                                                                                        | —        |
| 5    | 実装                   | —                                                                                                                        | —        |

ドメインを扱う場合はチャット頭に `#domain health` 等を宣言すれば AI が追読します。

-----

### 6️⃣ 今すぐ片づける Stage-1 タスク（抜粋）

| id                                     | purpose  | 説明                        |
| -------------------------------------- | -------- | ------------------------- |
| layer\_split\_migration                | obs      | 四階層フォルダへ移動 & `imports:` 追記 |
| profile\_yaml\_add                     | obs      | `legislation/personal/profile.yaml` 追加  | \# パスを更新
| template\_seed & domain\_folder\_setup | obs      | 共通テンプレ / domain フォルダ生成    |
| layer\_ci\_lint\_rule                  | obs      | `constitution/common/`↔`legislation/personal/` 重複禁止 Lint | \# パスを更新
| ci\_decision\_link\_check              | obs      | Decision↔Task ID CI       |
| kpi\_sheet\_add\_profit\_col           | value    | KPI「収益／貢献」列追加             |
| ci\_add\_g009\_lint                    | security | G009 静的解析ジョブ              |

-----

### 7️⃣ **同梱する 7 ファイル**（最新版）

| \# | path                                          | 目的                          |
| - | --------------------------------------------- | --------------------------- |
| 1 | `legislation/personal/profile.yaml`           | 固定属性                        | \# パスを更新
| 2 | `legislation/personal/core_principles.yaml`   | 要約＋Traceability             | \# パスを更新
| 3 | `legislation/personal/projects/os_platform.yaml` | 開発プロジェクト                    | \# パスを更新
| 4 | `records/task_log.yaml`                       | タスク                         | \# パスを更新
| 5 | `records/decision_log.yaml`                   | 意思決定                        | \# パスを更新
| 6 | `constitution/common/constitution.yaml`       | 憲法フル版                       | \# パスを更新
| 7 | `legislation/common/taxonomy.yaml`            | obs/value/security/speed 一覧 | \# パスを更新

*(`legislation/common/projects/project_template.yaml`・`legislation/common/domains/domain_template.yaml`・`legislation/personal/domains/health.yaml` は**同梱しても良い**ですが、AI は上位 7 ファイルで復元できます)*

-----

#### 👉 **新チャット開始手順**

```
1. 上の 7 ファイル + このメモを貼る
2. Human: 「作業を始めます」
   （任意）#project os_platform_v1   #domain health
3. AI がブリーフィング（todo一覧・Decision要約・推奨タスク）を返す
```

これで **四階層構造・普遍＆個人分割 + ドメイン + タクソノミー** を前提に、
ステートレス儀式で *デジタルツインOSプラットフォーム* / *書籍執筆プロジェクト* / *継続ドメイン* をシームレスに進行できます。

