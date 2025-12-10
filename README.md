# CATERYA — Ethical AI Evaluation Framework

> *If scientific truth isn't enough to judge an AI, how do we formulate ethics that are measurable — and actionable — without losing sight of the complexity of the human context?*
“What does it mean to trust a machine? If trust is a relation, then we must measure its shape.”  
> — A practical and philosophical question for AI evaluation design.

## Why?
Many AI audits are ad hoc; CATERYA exists to connect technical evaluations with social impact—and to do so systematically and transparently.

## What?
CATERYA is a Python toolkit (PyTorch/transformers compatible) for:
- calculating fairness and bias metrics (group and individual),
- measuring transparency and interpretability (SHAP, attribution),
- reporting citation metrics and fork analysis for models/datasets (repo metadata extraction),
- performing reproducible benchmarking and ablation,
- deploying automated evaluation pipelines using GitHub Actions and Docker.

## How? (Methodology Summary & Repo Structure)
- Modular Python package contained: metrics, interpretability, dataset, utils.
- Self-contained setup: `Dockerfile`, `requirements.txt`, synthetic dataset generator.
- CI & release pipeline via GitHub Actions:
  - lint, unit tests, static checks, run micro-benchmarks.
  - build Docker image & publish to registry; optional publish docs.
- Visuals: architecture diagrams (Mermaid), physics-inspired visualizations (energy landscapes untuk fairness loss).
- Documentation: white-paper README, `docs/` (math.md, benchmarks.md), Jupyter quickstart.

See `docs/` and `COLLABORATION_PATHWAY.md` for full white-paper style documentation.

## Self-Contained Execution
- `requirements.txt` (deterministic versions)
- `Dockerfile` untuk reproduceable env
- Synthetic dataset generator
- Example pipeline & demo script (`examples/run_demo.py`)
- GitHub Actions workflows

## Mathematical Formulation
See `docs/math.md`.

## Collaboration Pathway
**Technical expertise needed**: ML Engineers, Fairness Researchers, Data Engineers, DevOps, UX, Domain Experts.

**Strategic partners (examples)**:
- ITB, UGM, BRIN, Kominfo (Indonesia)
- Partnership on AI, The Alan Turing Institute, Stanford HAI (international)

**Commercialization & Models**: SaaS auditing, Consultancy & Certification, On-prem licensed deployments, Research grants.