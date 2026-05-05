# Hi, I'm Pouya 👋

I'm an MSc researcher in **Computer Engineering (AI)** at the University of Genoa,  
working as a Research Assistant at **CNR** within the EU Horizon Europe project [REXASI-PRO](https://rexasi-pro.spindoxlabs.com/).

My thesis investigates the reliability of pretrained neural motion prediction models  
for autonomous wheelchair navigation — understanding *when and why* they fail under varying input conditions.

---

## 🔬 Research Projects

### 🔹 [TrustRAG](https://github.com/pouyapd/TrustRAG) — Production RAG with Systematic Evaluation

![Tests Passing](https://raw.githubusercontent.com/pouyapd/TrustRAG/main/docs/screenshots/tests-passing.png)

End-to-end Retrieval-Augmented Generation system with a built-in evaluation 
and failure analysis framework.

- Failure-mode classifier tagging every output as one of 6 interpretable types  
  (`no_retrieval`, `wrong_retrieval`, `hallucination`, `refusal_when_answerable`, `partial_answer`, `ok`)
- Retrieval metrics: Precision@k, Recall@k, MRR
- LLM-as-judge faithfulness scoring
- Pluggable backends: OpenAI · Anthropic · local Ollama

**Benchmark:** Recall@k 0.90 · MRR 0.83 · Latency 2.4ms · 37 tests · CI on every commit

**Stack:** Python · FastAPI · ChromaDB · Docker · GitHub Actions

### 🔹 Trajectory Failure Analysis — Interpretable Risk Modeling for Motion Prediction

**Preprint (PDF available)** — ETH Pedestrian Dataset

A model-agnostic framework for analyzing failure modes in trajectory prediction systems, evaluated on real-world pedestrian data.

- Input-space sensitivity analysis (orientation–velocity risk regions)
- Interpretable decision tree models for failure rule extraction
- Cross-scene generalization analysis (ETH vs Hotel)

**Key Insight:** Initial orientation is a dominant global risk factor, while positional features are scene-dependent — indicating limited transferability of failure rules.

📄 [Read Paper](https://github.com/pouyapd/trajectory-failure-analysis/blob/main/paper.pdf)  
📊 [Code & Experiments](https://github.com/pouyapd/trajectory-failure-analysis)
![Cross-scene failure analysis](https://raw.githubusercontent.com/pouyapd/trajectory-failure-analysis/main/comparison_scenes.png)

### 🔹 [SafeTraj-Experiments](https://github.com/pouyapd/SafeTraj-Experiments)
**MSc Thesis — University of Genoa / CNR / REXASI-PRO**

Trajectory-level evaluation of pretrained DNN-LNA neural models for autonomous wheelchair navigation.

- Input sensitivity analysis — orientation φ is the dominant risk factor (failures near ±π)
- Goal difficulty mapping — spatial failure patterns across the workspace
- Comparative evaluation of 5 neural architectures (success rates: 25.3% → 99.3%)

**Demo:** [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pouyapd/SafeTraj-Experiments/blob/main/notebooks/demo_analysis.ipynb)

![Theta vs Distance](https://raw.githubusercontent.com/pouyapd/SafeTraj-Experiments/main/results/figures_exp1/exp1_theta_vs_distance.png)

---

### 🔹 [SafeTraj-Prototype](https://github.com/pouyapd/SafeTraj-Prototype) — [🔴 Live Demo](https://safetraj-prototype-auhavyacsp7udguqdsezhm.streamlit.app/)
**Trajectory Behaviour Analysis Toolkit**

Modular Python toolkit for trajectory risk scoring, failure-case analysis, and interpretable ML explanations.  
Includes an interactive Streamlit dashboard — try it live!

![SafeTraj Dashboard](https://raw.githubusercontent.com/pouyapd/SafeTraj-Prototype/main/assets/dashboard_high_risk.png)

- REST API endpoint for trajectory risk scoring (FastAPI)

---

### 🔹 [SafeNav-RL](https://github.com/pouyapd/SafeNav-RL)
**Safety-Constrained RL for Assistive Robot Navigation**

PPO agent with CBF safety layer and curriculum learning for obstacle avoidance navigation.

![SafeNav-RL Demo](https://raw.githubusercontent.com/pouyapd/SafeNav-RL/main/assets/trajectory_2.png)

---

## 📊 Other Projects

### 🔹 [superstore-analysis](https://github.com/pouyapd/superstore-analysis)
End-to-end BI workflow — Python, SQL, and Power BI dashboard.

![Superstore Dashboard](https://raw.githubusercontent.com/pouyapd/superstore-analysis/main/Screenshots/SalesbyRegion.jpg)

---

## 🔧 Tech Stack

**AI & ML** — Python · PyTorch · scikit-learn · NumPy · pandas  
**RL** — PPO · Gymnasium · CBF safety constraints  
**Tools** — Git · Streamlit · ROS2 · SQL · Power BI · TensorBoard

---

## 📫 Contact

🔗 [LinkedIn](https://www.linkedin.com/in/pouya-pourmand-021654325)  
📧 pouyapd68@gmail.com
