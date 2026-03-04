# Hi, I'm Pouya 👋

I'm an M.Sc. student in **Artificial Intelligence** at the University of Genoa,  
and a Research Assistant at **CNR-IEIIT** within the EU Horizon project [REXASI-PRO](https://rexasi-pro.spindoxlabs.com/).

My research focuses on **safety-critical AI**, **trajectory prediction reliability**,  
and **learning-based robot navigation** for assistive mobility systems (smart wheelchairs).

I'm interested in understanding *when and why* AI models fail — and building systems that are safe by design, not just accurate on average.

---

## 🔬 Research Projects

### 🔹 [SafeTraj-Experiments](https://github.com/pouyapd/SafeTraj-Experiments)
**MSc Thesis Research — University of Genoa / CNR-IEIIT**

Systematic analysis of neural trajectory prediction models for safety-critical assistive navigation.  
Focus on failure mode detection, input sensitivity, and interpretable risk patterns.

**Key findings:**
- Orientation (θ) is the dominant risk factor — failures concentrate near ±π
- Failure-distance metric reveals severity beyond simple success/failure labeling
- XAI supervisor (Random Forest ~98%) identifies unsafe input regions

#### Goal Difficulty Map
Identifies which target regions are inherently high-risk for neural predictors.
![Goal Difficulty Map](https://raw.githubusercontent.com/pouyapd/SafeTraj-Experiments/main/results/figures_exp2/exp2_goal_difficulty_map_avg.png)

#### Orientation Sensitivity (θ vs Distance)
Shows that initial orientation is the dominant factor influencing unsafe predictions.
![Theta Sensitivity](https://raw.githubusercontent.com/pouyapd/SafeTraj-Experiments/main/results/figures_exp1/exp1_theta_vs_distance.png)

---

### 🔹 [SafeNav-RL](https://github.com/pouyapd/SafeNav-RL)
**Safety-Constrained Reinforcement Learning for Assistive Robot Navigation**

Extends the failure analysis from SafeTraj-Experiments by training RL agents that are **intrinsically safe** — not just evaluated post-hoc.  
Uses PPO with a Control Barrier Function (CBF) safety layer, curriculum learning, and ROS2 deployment scaffold.

- CBF-inspired safety layer projects unsafe actions before execution
- Curriculum learning: agent advances through 3 difficulty stages automatically
- Domain randomization for sim-to-real robustness
- ROS2 node scaffold for real robot deployment

---

### 🔹 [SafeTraj-Prototype](https://github.com/pouyapd/SafeTraj-Prototype)
**Trajectory Behaviour Analysis Toolkit**

A lightweight Python toolkit for evaluating stability and reliability of neural trajectory predictors.  
Built as part of the REXASI-PRO project.

- Trajectory risk scoring and failure-case cataloguing
- Interpretable ML explanations via decision trees and random forests
- Interactive Streamlit dashboard for real-time exploration
- Optional LLM-based natural language safety reports

![SafeTraj Dashboard](https://raw.githubusercontent.com/pouyapd/SafeTraj-Prototype/main/assets/dashboard_high_risk.png)

---

## 📊 Other Projects

### 🔹 [superstore-analysis](https://github.com/pouyapd/superstore-analysis)
A complete BI workflow with Python data cleaning, SQL validation, and interactive Power BI dashboard.

![Superstore Dashboard](https://raw.githubusercontent.com/pouyapd/superstore-analysis/main/Screenshots/SalesbyRegion.jpg)

---

## 🔧 Tech Stack

**AI & Machine Learning**  
Python · PyTorch · scikit-learn · NumPy · pandas · OpenCV

**Reinforcement Learning**  
PPO · policy gradient methods · custom Gym environments · safety-constrained RL

**Research & Explainability**  
XAI · decision trees · random forests · failure analysis · risk estimation · uncertainty quantification

**Tools & Deployment**  
Git · Jupyter · Streamlit · ROS2 · SQL · Power BI · TensorBoard

---

## 📫 Contact

🔗 LinkedIn: https://www.linkedin.com/in/pouya-pourmand-021654325  
📧 Email: pouyapd68@gmail.com
