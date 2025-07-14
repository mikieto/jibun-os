
-----

# Architecture Overview: デジタルツインOS v3.0

## 1\. 概要 (Overview)

デジタルツインOSは、「コピー可能な自己（The Reproducible Self）」、すなわち「他者が読んでも学習可能な、再現性のある思考構造」を構築するために設計された、個人向けの自己進化型オペレーティングシステムです。この概念は、ご自身の思考や経験をデジタル空間に「双子」として忠実に再現し、それを観察・シミュレーションすることで自己への気づきと成長を加速させることを目指します。バージョン3.0では、AI協働、プロンプトエンジニアリング、セカンドブレインの知見を統合し、高モジュール化されたフレームワークとして再構築されました。

本アーキテクチャは、\*\*「普遍的なフレームワーク（共通コンポーネント）」**と**「個人的な実装（個人コンポーネント）」\*\*を明確に分離することで、OSの再利用性、拡張性、および保守性を飛躍的に向上させています。

## 2\. 四階層モデルによるディレクトリ構造 (Four-Layer Model Directory Structure)

システム全体は、デジタルツイン憲章で定義された以下の四階層モデルに基づき、ディレクトリ構造で構成されます。

  * **`constitution/`**: OSの最高規範となる普遍的な憲法と、OS所有者個人の核となる価値観を格納します。
  * **`legislation/`**: 憲法に基づいた具体的な運用ルール、フレームワーク、テンプレート、および個別の設定やプロジェクト/ドメイン定義を格納します。
  * **`precedents/`**: 個々の経験や記録から抽出された、より抽象化された知識や行動パターンを格納します。（現在は空）
  * **`records/`**: OSの運用中に動的に生成される、行動や決定に関するログデータを格納します。

<!-- end list -->

```
repo-root/
├─ constitution/            # 憲法・魂 (四階層モデルのL1)
│   ├─ common/
│   │   └─ constitution.yaml # OSフレームワークの最高規範（普遍的憲法）
│   └─ personal/
│       └─ constitution.yaml # あなた個人の憲法（究極の目的と価値観）
│
├─ legislation/             # 法律・知恵 (四階層モデルのL2)
│   ├─ common/
│   │   ├─ immune_system.yaml        # 知的免疫システムの普遍的フレームワーク
│   │   ├─ innate_immunity.yaml      # 普遍的なガードルール（生得免疫系）
│   │   ├─ mappings.yaml             # 原則とガード等の関連性定義
│   │   ├─ implementation_framework.yaml # 実装ガイドの各フレームワーク定義
│   │   ├─ taxonomy.yaml             # OS全体で共有されるタグや分類
│   │   ├─ prompt_patterns.yaml      # (計画中) 標準化されたプロンプトの型
│   │   ├─ projects/
│   │   │   └─ project_template.yaml # 普遍的なプロジェクトテンプレート
│   │   └─ domains/
│   │       └─ domain_template.yaml  # 普遍的なドメインテンプレート
│   └─ personal/
│       ├─ core_principles.yaml # 個人的な実装設定、役割、バックログなど
│       ├─ acquired_immunity.yaml # 個人的な獲得免疫ルール
│       ├─ profile.yaml             # あなたの固定的なプロフィール
│       ├─ projects/
│       │    ├─ os_platform.yaml     # このデジタルツインOS開発プロジェクトの定義
│       │    └─ book_writing.yaml    # 書籍執筆プロジェクトの定義
│       └─ domains/
│            └─ learning.yaml        # あなたの学習領域に関する定義
│
├─ precedents/              # 判例・意識 (四階層モデルのL3)
│   # (現在、ファイルなし。将来的に記録から抽出されたパターンを配置)
│
├─ records/                 # 記録・経験 (四階層モデルのL4)
│   ├─ task_log.yaml        # タスクの進捗ログ
│   ├─ decision_log.yaml    # 意思決定の記録
│   └─ guard_log.yaml       # ガードの発動記録
│
├─ docs/                    # ドキュメント (このファイル含む)
│   ├─ architecture_overview.md (本ファイル)
│   └─ charter.md             # デジタルツイン憲章 (v3.0)
│
├─ .github/                 # CI/CD関連
│   └─ workflows/
│       └─ validate.yaml
│
├─ system_map.yaml          # デジタルツインOS全体のファイル構造と役割を定義するマップ
└─ ... (その他の設定ファイル: .gitignore, README.md, requirements.txt など)
```

## 3\. 主要コンポーネントとその役割 (Key Components and Their Roles)

### 3.1. `constitution/common/` および `legislation/common/` ディレクトリ配下（普遍的フレームワーク）

  * **`constitution/common/constitution.yaml`**: デジタルツインOSの最高規範であり、普遍的な目的 (`supreme_purpose`)、核となる原則 (`core_code`)、AIとの関係性 (`ai_relationship`)、OS自体の進化に関するメタルール (`meta_rule`)、そして普遍的な運用原則（UOPs）を定義します。AIは従順なアシスタントではなく、OSの健全性を保つための「拮抗的パートナー」と位置づけられています。
  * **`legislation/common/immune_system.yaml`**: デジタルツインOSの自己防衛・自己成長メカニズム（生得免疫系）を定義する、普遍的なフレームワークです。
  * **`legislation/common/innate_immunity.yaml`**: OS所有者の思考や行動が憲法の原則から逸脱するのを防ぐための「保護機能」である、普遍的なガードルールを定義します。
  * **`legislation/common/mappings.yaml`**: `core_code` の各原則と、それを保護する`innate_immunity`の`universal_guards`間の紐付け (`guard_map`) など、異なるコンポーネント間の関連性を定義し、トレーサビリティを確保します。
  * **`legislation/common/implementation_framework.yaml`**: デジタルツインOSを実際に運用し、自己進化のサイクルを駆動させるための、標準的なプロセスとツールの「枠組み」を定義します。具体的な運用ステップやKPI項目は含まず、概念的なフレームワークを提供します。
  * **`legislation/common/taxonomy.yaml`**: `severity_levels` や `rule_types` など、デジタルツインOS全体で共有される分類体系や統制された語彙を定義します。

### 3.2. `constitution/personal/` および `legislation/personal/` ディレクトリ配下（個人実装）

  * **`constitution/personal/constitution.yaml`**: あなた個人のデジタルツインOSの魂とも言えるファイルです。あなたの究極の目的、核となる価値観、そしてOS運用の根源的な動機を定義します。
  * **`legislation/personal/core_principles.yaml`**: あなた個人のデジタルツインOSの具体的な実装設定、役割定義、監視すべき認知バイアス (`guard_details`)、および具体的なKPI指標 (`kpi_metrics`)、OS改善バックログなどを定義します。`constitution/common/constitution.yaml`や`legislation/common/`の各フレームワークをインポートして使用します。
  * **`legislation/personal/profile.yaml`**: OS所有者の固定的な属性（名前、タイムゾーン、使用ツールなど）を定義します。
  * **`legislation/personal/projects/os_platform.yaml`**: このデジタルツインOSプラットフォーム自体の開発に関するプロジェクト定義、現在のバージョン、ステージを管理します。（開発バックログは`legislation/personal/core_principles.yaml`に統合済み）
  * **`legislation/personal/acquired_immunity.yaml`**: あなたの具体的な失敗経験から学んだ、あなただけの特異的なルール（抗体）を蓄積します。

### 3.3. `records/` ディレクトリ配下（運用ログ）

  * **`records/task_log.yaml`**: デジタルツインOSの運用や改善における各タスクのID、ステージ、目的、説明、ステータス、関連する意思決定を記録します。
  * **`records/decision_log.yaml`**: 重要な意思決定の「なぜ」（理由）、選択肢、最終決定、および関連するタスクを記録し、Decision-Action Traceability (決定と行動の追跡可能性) を保証します。
  * **`records/guard_log.yaml`**: ガードが発動した際の記録や、AIとの対話履歴などを動的に記録します。

## 4\. 設計思想 (Design Philosophy)

本アーキテクチャは、以下の主要な設計思想に基づいています。

  * **再現可能な自己 (The Reproducible Self)**: 思考を外部化・構造化し、再現性のある形で記録することで、意識的な自己進化を可能にします。この概念は、個人の思考や経験をデジタル空間に「双子」として忠実に再現し、シミュレーションすることを通じた自己理解を深めます。
  * **AIとの拮抗的パートナーシップ**: AIを単なるツールではなく、OSの健全性を保ち、より高いレベルでの協働を実現するための生産的な緊張関係を持つパートナーと位置づけます。AIは思考の限界を超え、成長を加速させます。
  * **高モジュール化と再利用性**: 普遍的なフレームワークと個人的な実装を分離することで、OSの各コンポーネントを独立して管理・進化させ、他者への共有や拡張を容易にします。
  * **可観測性とトレーサビリティ**: 全ての決定と行動がログとして記録され、KPIによって定量的に把握されることで、OSの働きを可観測化し、自己改善のフィードバックループを強化します。
  * **不完全性の受容と戦略的活用**: 自身の弱点や認知バイアス（影）をOSに記述し、それを管理・補完する戦略を立てることで、完璧を目指さず、不完全な自己を効果的に運用します。

-----