# Hi, I'm Pouya 👋

I'm an M.Sc. student in **Artificial Intelligence** at the University of Genoa,  
and a Research Assistant at **CNR-IEIIT** within the EU Horizon project [REXASI-PRO](https://rexasi-pro.spindoxlabs.com/).

My research focuses on **reliability and interpretability of ML models** for trajectory prediction  
in safety-critical autonomous systems (smart wheelchairs, mobile robots).

I'm interested in understanding *when and why* models fail under distribution shifts and abnormal inputs —  
and building interpretable tools that make model behavior transparent and trustworthy.

---

## 🔬 Research Projects

### 🔹 [SafeTraj-Experiments](https://github.com/pouyapd/SafeTraj-Experiments)
**MSc Thesis Research — University of Genoa / CNR-IEIIT**

Systematic evaluation of pretrained neural trajectory prediction models under varying operational conditions.  
Focus on failure mode identification, input sensitivity analysis, and interpretable classification of safe vs unsafe trajectories.

**Key contributions:**
- Identified unsafe trajectory patterns arising from distribution shifts and abnormal inputs
- Applied decision trees, random forests, and k-NN to classify historical trajectories into safe/unsafe outcomes
- Orientation (θ) identified as dominant risk factor — failures concentrate near ±π
- Failure-distance metric quantifies severity beyond binary success/failure labeling

#### Goal Difficulty Map
Identifies which target regions are inherently high-risk for neural predictors.
![Goal Difficulty Map](https://raw.githubusercontent.com/pouyapd/SafeTraj-Experiments/main/results/figures_exp2/exp2_goal_difficulty_map_avg.png)

#### Orientation Sensitivity (θ vs Distance)
Shows that initial orientation is the dominant factor influencing prediction failures.
![Theta Sensitivity](https://raw.githubusercontent.com/pouyapd/SafeTraj-Experiments/main/results/figures_exp1/exp1_theta_vs_distance.png)

---

### 🔹 [SafeTraj-Prototype](https://github.com/pouyapd/SafeTraj-Prototype)
**Trajectory Behaviour Analysis Toolkit — REXASI-PRO Project**

A modular Python toolkit for evaluating stability and reliability of neural trajectory predictors  
for assistive navigation systems.

- Trajectory risk scoring and failure-case cataloguing
- Interpretable ML explanations via decision trees and random forests
- Interactive Streamlit dashboard for real-time trajectory exploration
- Optional LLM-based natural language safety reports

![SafeTraj Dashboard](https://raw.githubusercontent.com/pouyapd/SafeTraj-Prototype/main/assets/dashboard_high_risk.png)

---

### 🔹 [SafeNav-RL](https://github.com/pouyapd/SafeNav-RL)
**Safety-Constrained Reinforcement Learning for Assistive Robot Navigation**

An extension of my trajectory analysis work — training RL agents that incorporate  
collision avoidance constraints directly into the learned policy.

- PPO with Control Barrier Function (CBF) safety layer
- Curriculum learning across 3 difficulty stages
- Domain randomization for sim-to-real robustness
- ROS2 node scaffold for real robot deployment

---

## 📊 Other Projects

### 🔹 [superstore-analysis](https://github.com/pouyapd/superstore-analysis)
A complete BI workflow with Python data cleaning, SQL validation, and interactive Power BI dashboard.

![Superstore Dashboard](https://raw.githubusercontent.com/pouyapd/superstore-analysis/main/Screenshots/SalesbyRegion.jpg)

---

## 🔧 Tech Stack

**AI & Machine Learning**  
Python · PyTorch · scikit-learn · NumPy · pandas · OpenCV

**Research Focus**  
Model reliability evaluation · failure-case analysis · interpretable ML · trajectory prediction · uncertainty estimation

**Reinforcement Learning**  
PPO · policy gradient methods · custom Gym environments · safety-constrained RL

**Tools & Deployment**  
Git · Jupyter · Streamlit · ROS2 · SQL · Power BI · TensorBoard

---

## 📫 Contact

🔗 LinkedIn: https://www.linkedin.com/in/pouya-pourmand-021654325  
📧 Email: pouyapd68@gmail.com
