# Hi, I'm Pouya 👋

I'm an MSc researcher in **Computer Engineering (AI)** at the University of Genoa,  
working as a Research Assistant at **CNR** within the EU Horizon Europe project [REXASI-PRO](https://rexasi-pro.spindoxlabs.com/).

My thesis investigates the reliability of pretrained neural motion prediction models  
for autonomous wheelchair navigation — understanding *when and why* they fail under varying input conditions.

---

## 🔬 Research Projects

### ⭐ [TrustRAG](https://github.com/pouyapd/TrustRAG) — Evidence-Aware Evaluation and Failure Attribution for RAG

*Primary research project. Empirical study + reproducible evaluation framework.*

[![CI](https://github.com/pouyapd/TrustRAG/actions/workflows/ci.yml/badge.svg)](https://github.com/pouyapd/TrustRAG/actions/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/tests-466%20passing-brightgreen)](https://github.com/pouyapd/TrustRAG)
[![Coverage](https://img.shields.io/badge/coverage-80%25-green)](https://github.com/pouyapd/TrustRAG)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/pouyapd/TrustRAG/blob/main/LICENSE)

RAG evaluations report whether a chunk from the right *document* was retrieved.
That is not the same question as whether the passage supporting the answer
reached the generator — and the difference decides which pipeline stage a failure
is charged to.

![TrustRAG pipeline and evaluation layer](https://raw.githubusercontent.com/pouyapd/TrustRAG/main/docs/figures/pipeline_evaluation.png)

**Findings, measured on four public corpora (QASPER, Natural Questions,
HotpotQA, 2WikiMultihopQA):**

- **Attribution flips with the definition of retrieval success.** On Natural
  Questions, the same stored run charges **1** of 300 failures to retrieval at
  document level and **81** at evidence level.
- **Two separable blind spots.** A *granularity* gap on long documents
  (16.6–26.7 pp, p < 1e-14) and a *quantifier* gap on multi-hop questions
  (48.7 pp on HotpotQA, replicated at 64.7 pp on 2WikiMultihopQA), each null
  where the other dominates — robust across 4 embedders, 5 retrieval depths and
  4 chunk sizes.
- **Evidence-gated attribution agrees better with an independent annotation.**
  Scored against the same 200 annotated units: accuracy **0.805 vs 0.740**,
  Cohen's kappa **0.631 vs 0.573**, exact McNemar **p = 0.0294** (22 vs 9
  discordant). Of the 30 units the document gate misattributes to generation,
  22 had no gold evidence retrieved at all.
- **A measurement-integrity finding.** A 600-character display truncation in the
  annotation tool hid ~49% of the retrieved evidence (941/1000 chunks) and biased
  labels toward blaming retrieval. Audited, fixed, and regression-tested;
  restoring full context moved 13 of 200 labels, all in the predicted direction.

**Method:** character offsets carried chunker → vector store → retrieval, so
evidence coverage is interval arithmetic rather than string matching; a 9-category
versioned failure taxonomy with the fired rule recorded per row; blinded
stratified annotation packages with an offline annotation tool; Wilson intervals,
bootstrap and exact McNemar throughout.

*Provenance note: the 200-unit reference annotation was produced by human annotators following the written guidelines, using the full-context blinded annotation interface. The repository reports agreement with this independent human annotation and uses it as the reference set for evaluation*

**Stack:** Python · FastAPI · ChromaDB · sentence-transformers · Docker ·
GitHub Actions · pytest · Prometheus

📊 [Repository](https://github.com/pouyapd/TrustRAG) · 📄 [Research documentation](https://github.com/pouyapd/TrustRAG/tree/main/docs/paper) · 🧭 [Failure taxonomy](https://github.com/pouyapd/TrustRAG/blob/main/docs/TAXONOMY.md) · 🔬 [Experiments](https://github.com/pouyapd/TrustRAG/blob/main/docs/EXPERIMENTS.md)

---

### 🔹 [Trajectory Failure Analysis](https://github.com/pouyapd/trajectory-failure-analysis) — Interpretable Risk Modeling for Motion Prediction
**Preprint (PDF available)** — ETH Pedestrian Dataset

A model-agnostic framework for analyzing failure modes in trajectory prediction systems, evaluated on real-world pedestrian data.

- Input-space sensitivity analysis (orientation–velocity risk regions)
- Interpretable decision tree models for failure rule extraction
- Cross-scene generalization analysis (ETH vs Hotel)

**Key Insight:** Initial orientation is a dominant global risk factor, while positional features are scene-dependent — indicating limited transferability of failure rules.

📄 [Read Paper](https://github.com/pouyapd/trajectory-failure-analysis/blob/main/paper.pdf)  
📊 [Code & Experiments](https://github.com/pouyapd/trajectory-failure-analysis)

![Cross-scene failure analysis](https://raw.githubusercontent.com/pouyapd/trajectory-failure-analysis/main/comparison_scenes.png)

---

### 🔹 [SafeTraj-Experiments](https://github.com/pouyapd/SafeTraj-Experiments)
**MSc Thesis — University of Genoa / CNR / REXASI-PRO**

Trajectory-level analysis of pretrained DNN-LNA models for autonomous wheelchair navigation, focusing on reliability, failure analysis, and interpretable evaluation.

- Input-space sensitivity analysis identifying critical failure regions
- Goal-based difficulty mapping across the navigation workspace
- Explainable failure modelling using Decision Trees
- Comparative evaluation of 5 DNN-LNA models (25.3%–99.3% success rate)

**Demo:** [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pouyapd/SafeTraj-Experiments/blob/main/notebooks/demo_analysis.ipynb)

![Goal Difficulty Map](https://raw.githubusercontent.com/pouyapd/SafeTraj-Experiments/main/results/figures_exp2/exp2_goal_difficulty_map_avg.png)

---

### 🔹 [SafeTraj-Prototype](https://github.com/pouyapd/SafeTraj-Prototype) — [🔴 Live Demo](https://safetraj-prototype-auhavyacsp7udguqdsezhm.streamlit.app/)
**Trajectory Behaviour Analysis Toolkit**

Modular Python toolkit for trajectory risk scoring, failure-case analysis, and interpretable ML explanations.  
Includes an interactive Streamlit dashboard — try it live!

![SafeTraj Dashboard](https://raw.githubusercontent.com/pouyapd/SafeTraj-Prototype/main/assets/dashboard_high_risk.png)

- REST API endpoint for trajectory risk scoring (FastAPI)

---

## 📊 Other Projects

### 🔹 [superstore-analysis](https://github.com/pouyapd/superstore-analysis)
End-to-end BI workflow — Python, SQL, and Power BI dashboard.

![Superstore Dashboard](https://raw.githubusercontent.com/pouyapd/superstore-analysis/main/Screenshots/SalesbyRegion.jpg)

---

## 🔧 Tech Stack

**AI & ML** — Python · PyTorch · scikit-learn · NumPy · pandas  
**LLM & RAG** — OpenAI API · Anthropic API · ChromaDB · sentence-transformers · FastAPI  
**MLOps** — Docker · GitHub Actions CI · pytest · Prometheus · structlog . Git

---

## 📫 Contact

🔗 [LinkedIn](https://www.linkedin.com/in/pouya-pourmand-021654325)  
📧 pouyapd68@gmail.com
