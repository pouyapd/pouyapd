<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Pouya Bathaei Pourmand: trustworthy AI, ML evaluation, failure analysis, research software" src="assets/banner-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/pouya-pourmand-021654325"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Pouya%20Bathaei%20Pourmand-0a66c2?logo=linkedin&logoColor=white"></a>
  <a href="mailto:pouyapd68@gmail.com"><img alt="Email" src="https://img.shields.io/badge/email-pouyapd68%40gmail.com-59636e?logo=gmail&logoColor=white"></a>
  <a href="https://doi.org/10.5281/zenodo.19513187"><img alt="Preprint DOI" src="https://img.shields.io/badge/preprint-10.5281%2Fzenodo.19513187-1f6fcf"></a>
</p>

I work on **trustworthy AI**: evaluating machine-learning systems, finding out *where* and *why* they fail, and explaining those failures with interpretable models. I build this as tested, reproducible research software, and I report what the evidence does not show as clearly as what it does.

**MSc in Computer Engineering, University of Genoa (2026).** I was a Research Assistant (MSc thesis research) at **CNR-IEIIT** in the EU Horizon Europe project [REXASI-PRO](https://rexasi-pro.spindoxlabs.com/), working on the reliability of neural trajectory predictors for smart-wheelchair navigation.

**Research interests:** failure analysis of learned components in safety-critical systems · ML evaluation (black-box evaluation, risk maps, held-out checks, confidence intervals, honest baselines) · interpretable models as failure rules · safety filters for learned navigation · reproducible research software · evidence-level evaluation of retrieval-augmented generation.

## Selected work

<table>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/pouyapd/SafeTraj-Experiments"><img src="assets/projects/safetraj-experiments.png" alt="Strict success per orientation bin for five pretrained trajectory predictors" width="100%"></a>

**[SafeTraj-Experiments](https://github.com/pouyapd/SafeTraj-Experiments)** · MSc thesis

Black-box evaluation of five pretrained neural trajectory predictors for a smart wheelchair (REXASI-PRO): 200 sampled commands × 3 goals per model. Strict success ranged from **25.3 % to 99.3 %** under identical conditions; failures concentrate at initial orientations near ±π, and depth-4 decision trees turn them into explicit rules. 42 checks recompute the thesis numbers from the published files.

</td>
<td width="50%" valign="top">

<a href="https://github.com/pouyapd/trajectory-failure-analysis"><img src="assets/projects/trajectory-failure-analysis.png" alt="Binned risk maps for the ETH and Hotel scenes" width="100%"></a>

**[trajectory-failure-analysis](https://github.com/pouyapd/trajectory-failure-analysis)** · preprint

The same approach on real pedestrian trajectories (ETH dataset, 719 trajectories, two scenes) for a damped constant-velocity predictor. All 16 preprint values are reproduced from pinned raw data. Additional analyses show the limits: held-out tree accuracy does not exceed a constant baseline, and part of the positional signal in one scene is consistent with a horizon effect. [Preprint](https://doi.org/10.5281/zenodo.19513187), not peer-reviewed.

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/pouyapd/SafeTraj-Prototype"><img src="assets/projects/safetraj-prototype.png" alt="SafeTraj dashboard evaluating one command" width="100%"></a>

**[SafeTraj-Prototype](https://github.com/pouyapd/SafeTraj-Prototype)** · toolkit

The failure-analysis workflow as a reusable tool for any trajectory predictor: trajectory metrics and rule checks, input-novelty percentiles (reported separately from outcomes, because a typical input can still fail), risk maps and decision-tree failure rules. One implementation behind a Python library, CLI, FastAPI service and Streamlit dashboard, with 46 tests. Runs locally; the hosted API still serves version 1.

</td>
<td width="50%" valign="top">

<a href="https://github.com/pouyapd/SafeNav-RL"><img src="assets/projects/safenav-rl.png" alt="Trajectories of four controllers on the first three expert test scenarios" width="100%"></a>

**[SafeNav-RL](https://github.com/pouyapd/SafeNav-RL)** · simulation

PPO navigation agents with a discrete-time control-barrier-function speed filter, its proof and stated assumptions, and a seeded multi-seed benchmark. With the filter on there were **no collisions in 3,600 test episodes**; the cost is deadlock (expert success 94.6 % → 65.0 % when the filter is added). Training with the filter did not clearly help: 76.4 % vs 70.0 % with sampled actions, with overlapping intervals.

</td>
</tr>
</table>

### [TrustRAG](https://github.com/pouyapd/TrustRAG): evidence localisation and failure attribution for RAG evaluation

<a href="https://github.com/pouyapd/TrustRAG"><img src="assets/projects/trustrag.png" alt="TrustRAG pipeline and evaluation layer" width="100%"></a>

A measurement study of what happens *inside* the right document: retrieving the correct document is not the same as ranking the passage that supports the answer first.

- Seven localisers (BM25, dense bi-encoders and cross-encoder rerankers; 22M–278M parameters) on QASPER and Natural Questions, with a retrieval decomposition on four corpora.
- An author-conducted annotation of 200 QASPER units: gating failure attribution on span coverage agrees with the labels more often than gating on document coverage (accuracy 0.700 vs 0.600). One annotator: agreement with a guided expert reading, not independent validation.
- A defect found in my own BM25 baseline led to withdrawing an earlier result; the correction is kept on record in the repository.

Offset-carrying pipeline, failure taxonomy, Wilson intervals, exact McNemar with Holm correction, cluster bootstrap; 504 tests. Software and annotation data on Zenodo: [10.5281/zenodo.22879358](https://doi.org/10.5281/zenodo.22879358), [10.5281/zenodo.22879569](https://doi.org/10.5281/zenodo.22879569).

## Tools I use in these projects

- **ML and evaluation:** Python · PyTorch · scikit-learn · NumPy · pandas · SciPy · Gymnasium · Matplotlib
- **LLM and retrieval:** sentence-transformers · BM25 · cross-encoder rerankers · ChromaDB · OpenAI and Anthropic APIs
- **Software:** FastAPI · Streamlit · pytest · GitHub Actions · Docker · Prometheus · Git

## Other projects

- [superstore-analysis](https://github.com/pouyapd/superstore-analysis): end-to-end BI workflow with Python, SQL and Power BI.

## Contact

[LinkedIn](https://www.linkedin.com/in/pouya-pourmand-021654325) · pouyapd68@gmail.com

<sub>The banner's small drawings come from the projects' own committed results (generated by <a href="tools/make_portfolio_assets.py"><code>tools/make_portfolio_assets.py</code></a>); the project images are copies of figures and a screenshot from the repositories above.</sub>
