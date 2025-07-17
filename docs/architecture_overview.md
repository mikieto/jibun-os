<!-- docs/architecture_overview.md -->

# Architecture Overview: Jibun OS v3.1 — Prompt‑Ingestion × Digital‑Twin

## 1. Overview
Jibun OS は **Prompt‑Ingestion OS** (短期文脈) と **Digital‑Twin OS** (長期記憶) を統合した、自己進化型パーソナル OS である。

- *Prompt‑Ingestion layer* : VSCode/Cursor など IDE から直近コンテキストを即座に AI へ投入し、思考フローを加速。
- *Digital‑Twin layer*      : 四階層モデルに従いログ→知識→ポリシー→価値観を蓄積し、長期的な学習と説明責任を担保。

## 2. Directory Structure (Four‑Layer Model)

システム全体は、デジタルツイン憲章で定義された以下の四階層モデルに基づき、ディレクトリ構造で構成されます。

  * **`constitution/`**: OSの最高規範となる普遍的な憲法と、OS所有者個人の核となる価値観を格納します。
  * **`legislation/`**: 憲法に基づいた具体的な運用ルール、フレームワーク、テンプレート、および個別の設定やプロジェクト/ドメイン定義を格納します。
  * **`precedents/`**: 個々の経験や記録から抽出された、より抽象化された知識や行動パターンを格納します。（現在は空）
  * **`records/`**: OSの運用中に動的に生成される、行動や決定に関するログデータを格納します。

```
repo-root/
├─ constitution/ # L1 憲法・魂
│ └─ common/constitution.yaml # ← 本憲章 (Jibun OS Charter)
├─ legislation/ # L2 法律・知恵
│ ├─ common/
│ │ ├─ immune_system.yaml
│ │ └─ mappings/ # ← 今後分割されるディレクトリ
│ └─ personal/
│ └─ projects/os_platform.yaml
├─ precedents/ # L3 判例・意識
└─ records/ # L4 記録・経験
```

> **変更点:**
> • `system_map.yaml` の `description` を **"Prompt‑Ingestion & Digital‑Twin unified map"** に更新。
> • 旧 `mappings.yaml` は `legislation/common/mappings/` ディレクトリへ段階移行予定。

## 3. Key Components
- **Prompt‑Context Ingestor**
- **Vector‑RAG Cache**
- **Policy CI (OPA/Cedar)**
- **Knowledge Crystallizer (Zettel Engine)**

## 4. Design Philosophy
1. **Reproducible Self** — 再現可能な思考構造
2. **Synergistic Tension with AI** — AI と人の役割分担
3. **High Modularity & Reuse** — テンプレ／ガード再利用
4. **Observability & Traceability** — 四層で監査可能
5. **Strategic Embrace of Imperfection** — 不完全性を管理資産化

---

## Appendix – Glossary
| Term | Meaning |
|------|---------|
| **Prompt‑Ingestion OS** | Jibun OS の短期文脈層 |
| **Digital‑Twin OS** | Jibun OS の長期記憶層 |
| **Jibun OS** | 上記二層を統合した自己進化 OS |
