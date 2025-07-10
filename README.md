## 🆕「ゼロから再開」ミニパック – **三層 × 共通/固有分割 & 定型セッション**

v2025-07-11 r2 （domains / taxonomy / project template 対応）

> **このメモ＋下記 7 ファイル** を新チャットに貼れば、初見の AI でも同じ状況に復元し
> “Stateless 儀式” で **os\_platform** / **book\_writing** ─ さらに **継続ドメイン** まで扱えます。

---

### 1️⃣ プロジェクト識別 & 現在地

| key            | value                          |
| -------------- | ------------------------------ |
| project\_id    | **os\_platform\_v1**           |
| branch         | `feat/triple-layer`            |
| latest\_tag    | `v10.0.0-alpha.0` (PoC-1 DONE) |
| current\_stage | **1 / 5** — 基盤整備               |
| purpose\_short | *AI＋外部FBを高速循環し「学習データ→価値」を即転換*  |

---

### 2️⃣ ディレクトリ三層構造（共通 / personal それぞれに projects & domains）

```
repo-root/
├─ common/
│   ├─ core_principles.yaml          # 憲法フル版（下§3）
│   ├─ taxonomy.yaml                 # obs / value / security / speed
│   ├─ projects/
│   │    └─ project_template.yaml    # NEW: 万能プロジェクト雛形
│   └─ domains/
│        └─ domain_template.yaml     # 万能ドメイン雛形
├─ personal/
│   ├─ profile.yaml                  # 固定属性
│   ├─ core_principles.yaml          # 要約＋Traceability
│   ├─ projects/
│   │    ├─ os_platform.yaml
│   │    └─ book_writing.yaml        # stub
│   └─ domains/
│        └─ health.yaml              # 継続責任ドメイン例
└─ logs/
    ├─ task_log.yaml
    └─ decision_log.yaml
```

---

### 3️⃣ **common/core\_principles.yaml** – 初期内容（“普遍部分”のみ）

```yaml
---
version: "10.0.0"
last_updated: "2025-07-11"

constitution:
  supreme_purpose: >
    本OSは「コピー可能な自己」を構築し、
    AI と協働しながら主体的・倫理的に進化するための
    不変の原則を提供する。

core_code:
  - name: "How→Why 抽出アプローチ"
  - name: "実践的効果重視"
  - name: "誠実性と透明性"

guards:
  - id: "G001"    # 構造化ガード
  - id: "G002"    # 計画的完了ガード
  - id: "G006"    # Value-Engineering Guard
  - id: "G008"    # セキュリティ & レジリエンス
```

*個人バイアス監視 (G005 等) や Traceability 原則は **personal/core\_principles.yaml** 側で override します。*

---

### 4️⃣ **common/projects/project\_template.yaml**

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

### **common/domains/domain\_template.yaml**

```yaml
---
domain_id     : "<domain_id>"
purpose_short : "<continuous responsibility area>"
kpis: []
habits: []
default_tags  : ["obs","value","security"]
```

---

### 5️⃣ Stateless “セッション儀式” (読み込み順更新済み)

| Step | トリガー                 | AI が読む順序                                                                                                                 | 出力       |
| ---- | -------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------- |
| 0    | **Human**: “作業を始めます” | ① `personal/profile.yaml` → ② `personal/core_principles.yaml` → ③ `common/taxonomy.yaml` → ④ 選択 project → (任意) 指定 domain | —        |
| 1    | (自動) ブリーフィング         | todo 一覧 / Decision 要約 / 推奨タスク                                                                                            | Markdown |
| 2-4  | 選択→ドラフト→承認           | —                                                                                                                        | —        |
| 5    | 実装                   | —                                                                                                                        | —        |

ドメインを扱う場合はチャット頭に `#domain health` 等を宣言すれば AI が追読します。

---

### 6️⃣ 今すぐ片づける Stage-1 タスク（抜粋）

| id                                     | purpose  | 説明                        |
| -------------------------------------- | -------- | ------------------------- |
| layer\_split\_migration                | obs      | 三層フォルダへ移動 & `imports:` 追記 |
| profile\_yaml\_add                     | obs      | personal/profile.yaml 追加  |
| template\_seed & domain\_folder\_setup | obs      | 共通テンプレ / domain フォルダ生成    |
| layer\_ci\_lint\_rule                  | obs      | common↔personal 重複禁止 Lint |
| ci\_decision\_link\_check              | obs      | Decision↔Task ID CI       |
| kpi\_sheet\_add\_profit\_col           | value    | KPI「収益／貢献」列追加             |
| ci\_add\_g009\_lint                    | security | G009 静的解析ジョブ              |

---

### 7️⃣ **同梱する 7 ファイル**（最新版）

| # | path                                 | 目的                          |
| - | ------------------------------------ | --------------------------- |
| 1 | `personal/profile.yaml`              | 固定属性                        |
| 2 | `personal/core_principles.yaml`      | 要約＋Traceability             |
| 3 | `personal/projects/os_platform.yaml` | 開発プロジェクト                    |
| 4 | `logs/task_log.yaml`                 | タスク                         |
| 5 | `logs/decision_log.yaml`             | 意思決定                        |
| 6 | `common/core_principles.yaml`        | 憲法フル版                       |
| 7 | `common/taxonomy.yaml`               | obs/value/security/speed 一覧 |

*(common の project\_template.yaml・domain\_template.yaml・personal/domains/health.yaml は**同梱しても良い**ですが、AI は上位 7 ファイルで復元できます)*

---

#### 👉 **新チャット開始手順**

```
1. 上の 7 ファイル + このメモを貼る
2. Human: 「作業を始めます」
   （任意）#project os_platform_v1   #domain health
3. AI がブリーフィング（todo一覧・Decision要約・推奨タスク）を返す
```

これで **三層構造・共通＆personal分割 + domains + taxonomy** を前提に、
ステートレス儀式で *os\_platform* / *book\_writing* / *継続ドメイン* をシームレスに進行できます。
