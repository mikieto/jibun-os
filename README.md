# Jibun OS - A Personal OS for Self-Evolution

**“Jibun OS is a personal operating system, powered by a Prompt-Ingestion & Digital-Twin framework, designed to accelerate your learning loop and evolve with you.”**

---

## 🚀 Quick PoC: Initialize Your OS via AI Dialogue

### The Why Behind This Project

Our vision is to provide a "Reproducible Self" template to the world, empowering everyone with their own OS for self-evolution.

As the first step toward this vision, our immediate mission is to build an OS that accelerates our own learning loop, with a measurable goal of **reducing our decision-making cycle time by 30%**.

This PoC offers a glimpse into the core concept: operating your OS through a simple dialogue with an AI.

### Your 5-Minute Quick Start

1.  **Setup**
    Use this repository as a GitHub template to create your own. Then, open it in **GitHub Codespaces**.
    > Required dependencies are automatically installed via the `devcontainer` setup, ensuring a zero-config start.

2.  **Execution**
    Open the chat interface in VSCode/Cursor and say the following to the AI (me):
    > **"Initialize this OS for me."**

3.  **Result**
    The AI will ask for your name and other details, then automatically generate your personal configuration files (e.g., `legislation/personal/profile.yaml`). You will receive a confirmation message:
    > **"Initialization complete. I've created your profile at `legislation/personal/profile.yaml`."**

And that's it. The basic setup for your personal OS is now complete.

---

## 🏛️ Four-Layer Architecture

This OS is built on a four-layer governance model, separating timeless principles from daily records.

```

repo-root/
├─ constitution/            \# L1: The Soul (Core Principles)
│   ├─ common/
│   │   ├─ constitution.yaml
│   │   ├─ mvc\_v1.0.yaml
│   │   └─ udhr.yaml
│   └─ personal/
│       └─ constitution.yaml
│
├─ legislation/             \# L2: The Intellect (Rules & Policies)
│   ├─ common/
│   │   ├─ immune\_system.yaml
│   │   ├─ innate\_immunity.yaml
│   │   ├─ jurisprudence.yaml        \# NEW: General Legal Principles
│   │   ├─ kpi.yml                   \# NEW: KPI Definitions
│   │   ├─ implementation\_framework.yaml
│   │   ├─ taxonomy.yaml
│   │   └─ mappings/                 \# UPDATED: Separated Mappings
│   │       ├─ guards.yaml
│   │       ├─ field\_task\_decision.yaml
│   │       └─ ...
│   └─ personal/
│       ├─ core\_principles.yaml
│       ├─ acquired\_immunity.yaml
│       ├─ profile.yaml
│       └─ projects/
│           └─ os\_platform.yaml
│
├─ precedents/              \# L3: The Consciousness (Patterns)
│
├─ records/                 \# L4: The Experience (Logs)
│   ├─ task\_log.yaml
│   ├─ decision\_log.yaml
│   └─ guard\_log.yaml
│
├─ docs/                    \# Documentation
├─ .devcontainer/           \# Devcontainer for Codespaces
├─ .github/                 \# CI/CD Workflows
└─ system\_map.yaml          \# The single source of truth for the OS structure

```

---

## 🎯 Project Status (os_platform_v1)

* **Branch:** `feat/oss-launch-plan`
* **Current Phase:** `M0 – Stabilize`
* **Next Milestone:** Complete all M0 tasks by 2025-08-15.
* **License:** Apache-2.0
```
