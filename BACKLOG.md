
# 自分OS 開発バックログ（最終更新版）

| 優先度 (Priority) | カテゴリ (Category) | タスク名 (Task) | 目的・ゴール (Goal) | 関連ガード/原則 | 備考 (Status/Next Steps) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P1** | **CI/CD & Repository Health** | **CIスキーマ v1.5 反映** | Enum参照＆Guard ID一意性を含むv1.5スキーマが`main`に適用され、CIがパスしていることを確認する。 | `G008` | **完了済み** |
| **P1** | **Documentation & Onboarding** | **README拡充: activity_structure追記とCI要件の明記** | 新しい二重プロジェクト構造とLearning-LoopをOnboardingに反映し、スキーマv1.5の要件を明記する。 | `G001`, `Phase 2 Requirements` | **次の着手タスク** |
| **P2** | **Data Ops** | **Dog-foodingデータ収集開始** | Guard/KPIの実データを定期的に取得し、可視化する仕組みを構築する。 | `実践的効果重視`, `kpis` | |
| **P2** | **Outreach** | **外化モデルパイロット実装** | 最小ターゲットで1ループ検証し、Guard Logと紐付けを行う。 | `acceleration_strategies` | |
| **P2** | **Tooling & Automation** | **Guard Log連携スクリプトの設計** | `Guard_Activation_Log`シートへの記録を省力化・自動化する仕組み（Apps Script等）を設計し、データ蓄積のハードルを下げる。 | `実践的効果重視`, `kpis` | |
| **P2** | **Core Feature Enhancements** | **KPIの拡張と定量化** | `enhanced_kpis`案を参考に、KPIをより具体的で測定可能な指標（例：仮説→行動の時間）に進化させる。 | `可観測性`, `実践的効果重視` | |
| **P2** | **Documentation & Onboarding** | **ファイル分割（モジュール化）の検討** | OSのYAMLファイルを`core`, `implementation`, `common`などに分割し、可読性とメンテナンス性を向上させる。 | `G006`, `オーバーエンジニアリング検知ガード` | |
| **P3** | **Security/Ethics** | **セーフティモード運用手順ドキュメント作成** | 発動から復旧までのフローを明文化する。 | `G008`, `G009` | |
| **P3** | **CI/CD & Repository Health** | **スキーマ v1.6 設計 & 実装** | `threshold`の型を厳格化し、Guard Log側のEnum参照もバリデートできるようスキーマを設計・更新する。 | `G008`, `可観測性` | **追加タスク** |
| **P3** | **CI/CD & Repository Health** | **Guard Log Enum整合Lint導入** | `log_linking_guidelines.data_format_example.severity`が`common.severity_levels`に必ず一致する静的チェックをCIに追加する。 | `G008`, `可観測性` | **追加タスク** |
| **P3** | **Core Feature Enhancements** | **メタ認知レイヤーの導入** | `metacognitive_layer`案を基に、思考パターンの自動検出や認知の死角を可視化する、より高次の自己監視機能を設計する。 | `supreme_purpose`, `可観測性` | |
| **P3** | **Core Feature Enhancements** | **AI進化適応プロトコルの実装** | `ai_evolution_adaptation`案を基に、AIの能力向上を定期的に評価し、人間とAIの役割を再配分する仕組みを具体化する。 | `ai_relationship`, `meta_rule` | |
| **P3** | **Tooling & Automation** | **OSのAPI化** | ガード定義などをJSONとしてエクスポートするスクリプトを用意し、外部ツールからの参照を容易にする。 | `Phase 3 Requirements` | |
| **P3** | **Documentation & Onboarding** | **Phase 2 (MVP) 資料の作成** | 外部ユーザー向けのREADMEやランディングページのワイヤーフレームを作成し、他者への共有準備を開始する。 | `Phase 2 Requirements` | |
| **P3** | **Documentation & Onboarding** | **用語集（Glossary）の作成** | 「世界道場」などOS固有の用語を解説するドキュメントを作成し、外部ユーザーの理解を助ける。 | `Phase 2 Requirements` | |

