## Hi, I'm Pouya

I work on **trustworthy AI**: evaluating machine-learning systems, finding out *where* and *why* they fail, and explaining those failures with interpretable models. I build this as tested, reproducible research software.

MSc in Computer Engineering (Artificial Intelligence), University of Genoa. I was a Research Assistant (MSc thesis research) at **CNR-IEIIT** in the EU Horizon Europe project [REXASI-PRO](https://rexasi-pro.spindoxlabs.com/), working on the reliability of neural trajectory predictors for smart-wheelchair navigation.

**Research interests**

- **Trustworthy and safe AI** — failure analysis of learned components in safety-critical systems; safety filters
- **ML evaluation** — black-box evaluation, risk maps, held-out checks, confidence intervals, honest baselines
- **Interpretable and robust AI** — decision-tree surrogates as failure rules; input-novelty checks
- **Safety-aware navigation and reproducible research software** — seeded benchmarks, verification of published results
- **RAG evaluation** — a separate, related direction: evidence-level evaluation of retrieval-augmented generation

---

## Failure analysis of learned trajectory predictors

### [SafeTraj-Experiments](https://github.com/pouyapd/SafeTraj-Experiments) — MSc thesis

Black-box evaluation of five pretrained neural trajectory predictors (DNN-LNA, REXASI-PRO) for a smart wheelchair: 200 sampled commands × 3 goals per model. Strict success ranged from **25.3 % to 99.3 %** across models tested under identical conditions; failures concentrate in identifiable command regions, mainly initial orientations near ±π, and depth-4 decision trees turn them into explicit rules. The models are proprietary; the repository publishes the evaluation code and results, with a SHA-256 manifest and 42 checks that recompute the thesis numbers from the published files.

![Strict success per orientation bin for the five predictors](https://raw.githubusercontent.com/pouyapd/SafeTraj-Experiments/main/docs/figures/derived/orientation_sensitivity.png)

### [trajectory-failure-analysis](https://github.com/pouyapd/trajectory-failure-analysis) — preprint

The same approach on real pedestrian trajectories (ETH dataset, 719 trajectories, two scenes): risk maps and interpretable decision trees for a damped constant-velocity predictor (velocity × 0.98 per step). Initial orientation matters in both scenes, while the importance of position differs between them. A reproduction script re-creates the preprint's results table and quoted feature importances from the pinned raw data; additional, clearly separated analyses show the limits (held-out accuracy of the trees does not exceed a constant baseline; part of the positional signal in one scene is consistent with an effect of the varying prediction horizon).

Preprint: [doi:10.5281/zenodo.19513187](https://doi.org/10.5281/zenodo.19513187) (not peer-reviewed)

![Binned risk maps for the ETH and Hotel scenes](https://raw.githubusercontent.com/pouyapd/trajectory-failure-analysis/main/docs/figures/risk_maps_orientation_speed.png)

### [SafeTraj-Prototype](https://github.com/pouyapd/SafeTraj-Prototype) — toolkit

The failure-analysis workflow as a reusable tool for any trajectory predictor: trajectory metrics and rule checks, input-novelty scores with percentile thresholds (reported separately from outcomes — a typical input can still fail), batch CSV evaluation, comparisons, risk maps and decision-tree failure rules. One implementation behind a Python library, CLI, FastAPI service and Streamlit dashboard. [Hosted demo](https://safetraj-prototype-auhavyacsp7udguqdsezhm.streamlit.app/) · [hosted API docs](https://safetraj-api.onrender.com/docs) (free tier, slow first request; on 2026-10-11 the hosted API still ran version 1)

<img src="https://raw.githubusercontent.com/pouyapd/SafeTraj-Prototype/main/docs/figures/dashboard_evaluate.png" alt="SafeTraj dashboard" width="760">

---

## Safety-aware navigation

### [SafeNav-RL](https://github.com/pouyapd/SafeNav-RL) — reinforcement learning with a control-barrier-function safety filter (simulation)

A 2D navigation simulator with a range sensor, PPO agents, a discrete-time CBF speed filter with a stated forward-invariance guarantee (and its assumptions), two classical baselines and a seeded multi-seed benchmark. Across 3,600 test episodes with the filter on there were **no collisions**; the cost is deadlock — on the hardest stage the PPO agent trained without the filter falls from 94.6 % to 65.0 % success when the filter is added. Training with the filter in the loop did not clearly help: 61.0 % vs 65.0 % with the policy mean, and 76.4 % vs 70.0 % with sampled actions, with overlapping intervals. Simulation only; the ROS 2 node is an untested scaffold.

<img src="https://raw.githubusercontent.com/pouyapd/SafeNav-RL/main/docs/figures/hero_same_scenario.png" alt="Trajectories of four controllers on the first three expert test scenarios" width="760">

---

## RAG evaluation

### [TrustRAG](https://github.com/pouyapd/TrustRAG) — evidence localisation and failure attribution for RAG evaluation

[![CI](https://github.com/pouyapd/TrustRAG/actions/workflows/ci.yml/badge.svg)](https://github.com/pouyapd/TrustRAG/actions/workflows/ci.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22879357.svg)](https://doi.org/10.5281/zenodo.22879357)

A measurement study of what happens *inside* the right document: retrieving the correct document is not the same as localising the passage that supports the answer.

- Seven localisers (BM25, dense bi-encoders, cross-encoder rerankers; 22M–278M parameters) on QASPER and Natural Questions: rank-1 localisation **hit@1 0.29–0.51**, hit@5 0.69–0.86.
- Retrieval decomposition on four corpora: a *granularity* gap on long documents (16.6 pp QASPER, 26.7 pp NQ) and a *quantifier* gap on multi-hop questions (48.7 pp HotpotQA, 64.7 pp 2WikiMultihopQA), each null where the other dominates.
- Author-conducted annotation of 200 QASPER units: gating failure attribution on span coverage agrees with the labels more often than gating on document coverage (accuracy 0.700 vs 0.600, exact McNemar p = 3.6 × 10⁻⁵). One annotator — agreement with a guided expert reading, not independent validation.
- A defect found in my own BM25 baseline led to withdrawing an earlier result; the correction is kept on record in the repository.

Offset-carrying pipeline, failure taxonomy, Wilson intervals, exact McNemar with Holm correction, cluster bootstrap; 504 tests. Software and annotation data on Zenodo: [10.5281/zenodo.22879358](https://doi.org/10.5281/zenodo.22879358), [10.5281/zenodo.22879569](https://doi.org/10.5281/zenodo.22879569).

![TrustRAG pipeline and evaluation layer](https://raw.githubusercontent.com/pouyapd/TrustRAG/main/docs/figures/pipeline_evaluation.png)

---

## Other projects

- [superstore-analysis](https://github.com/pouyapd/superstore-analysis) — end-to-end BI workflow with Python, SQL and Power BI.

## Tech stack

**ML and evaluation** — Python · PyTorch · scikit-learn · NumPy · pandas · SciPy · Gymnasium · Matplotlib
**LLM and RAG** — sentence-transformers · ChromaDB · OpenAI and Anthropic APIs
**Software** — FastAPI · Streamlit · pytest · GitHub Actions · Docker · Prometheus · Git

## Contact

[LinkedIn](https://www.linkedin.com/in/pouya-pourmand-021654325) · pouyapd68@gmail.com
