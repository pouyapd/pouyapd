# Hi, I'm Pouya 👋

I'm an M.Sc. student in **Computer Engineering (Artificial Intelligence)** at the University of Genoa,  
and a Research Assistant at **CNR-IEIIT** within the EU Horizon Europe project [REXASI-PRO](https://rexasi-pro.spindoxlabs.com/).

My thesis focuses on **trajectory-level evaluation of neural motion prediction models**  
for autonomous wheelchair navigation — specifically, understanding *when and why*  
pretrained neural predictors generate unstable or unsafe trajectories under varying input conditions.

I work at the intersection of **model reliability analysis**, **interpretable evaluation frameworks**,  
and **safety-critical autonomous systems**.

---

## 🔬 Research Projects

### 🔹 [SafeTraj-Experiments](https://github.com/pouyapd/SafeTraj-Experiments)
**MSc Thesis — University of Genoa / CNR-IEIIT / REXASI-PRO**

Trajectory-level evaluation of pretrained neural wheelchair navigation models (DNN-LNA)  
across a wide range of operational input conditions.

**Two complementary experiments:**

- **Exp1 — Input Sensitivity:** How do initial orientation (φ), linear velocity (v), and angular velocity (ω) affect trajectory stability? Risk maps identify command regions prone to unstable predictions.
- **Exp2 — Goal Difficulty:** Which target positions are inherently harder for neural predictors? Goal difficulty maps reveal spatial failure patterns across the workspace.

**Key findings:**
- Initial orientation φ is the dominant risk factor — failures concentrate near ±π (robot facing away from goal)
- Strict vs. soft success criteria reveal stability differences between models invisible to binary metrics
- DNN-LNA-closs2 achieves 99.3% strict success; DNN-LNA-closs1 only 25.3%
- Risk maps enable concrete run-time safety applications: command filtering, hybrid fallback planners, predictive failure monitoring

#### Exp1 — Risk Map (Orientation vs Angular Velocity)
![Risk Map](https://raw.githubusercontent.com/pouyapd/SafeTraj-Experiments/main/results/figures_exp1/exp1_theta_vs_distance.png)

#### Exp2 — Goal Difficulty Map
![Goal Difficulty](https://raw.githubusercontent.com/pouyapd/SafeTraj-Experiments/main/results/figures_exp2/exp2_goal_difficulty_map_avg.png)

---

### 🔹 [SafeTraj-Prototype](https://github.com/pouyapd/SafeTraj-Prototype)
**Trajectory Behaviour Analysis Toolkit — REXASI-PRO Project**

A modular Python toolkit for evaluating stability and reliability of neural trajectory predictors  
in assistive navigation systems. Built alongside the thesis research.

- Trajectory risk scoring and failure-case cataloguing
- Interpretable ML explanations via decision trees and random forests
- Interactive Streamlit dashboard for real-time trajectory exploration
- Optional LLM-based natural language safety report generation

![SafeTraj Dashboard](https://raw.githubusercontent.com/pouyapd/SafeTraj-Prototype/main/assets/dashboard_high_risk.png)

---

### 🔹 [SafeNav-RL](https://github.com/pouyapd/SafeNav-RL)
**Safety-Constrained Reinforcement Learning for Assistive Robot Navigation**

A natural extension of the thesis work: rather than only analysing when neural predictors fail,  
this project trains RL agents with intrinsic collision-avoidance constraints from the ground up.

- PPO with Control Barrier Function (CBF) safety layer
- Curriculum learning across 3 progressive difficulty stages
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
Trajectory-level evaluation · model reliability · failure mode analysis ·  
interpretable ML · safety-critical autonomous systems · neural motion prediction

**Reinforcement Learning**  
PPO · policy gradient methods · custom Gym environments · safety-constrained RL

**Tools**  
Git · Jupyter · Streamlit · ROS2 · SQL · Power BI · TensorBoard

---

## 📫 Contact

🔗 LinkedIn: https://www.linkedin.com/in/pouya-pourmand-021654325  
📧 Email: pouyapd68@gmail.com
