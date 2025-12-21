Secure Network-aware Offloading Simulator (SNOS)

🚀 Project Overview

This simulator models the decision-making process for task offloading in a heterogeneous mobile network (Mobile -> D2D Proxy -> Edge Cloud). It evaluates the trade-offs between Accuracy, Latency, and Energy Consumption while enforcing a Machine Learning-driven security layer.

Key Features

Multi-Path Offloading: Supports Local NPU, D2D Proxy, and Edge Cloud paths.

Security-Aware: Integrated risk-check module that triggers fallback to Local NPU upon threat detection.

Policy Comparison: Compares Max_Accuracy, Max_Latency, and D2D_Utility strategies.

Energy Modeling: Calculates Joule consumption based on transmission power and compute intensity.

📊 Key Findings (Experimental Results)

Based on simulation runs of 1,000 tasks:

Policy

Avg. Accuracy

Avg. Latency (s)

Avg. Energy (J)

Decision Trend

Max Accuracy

0.9434

0.542

0.1250

Edge Cloud Heavy

Max Latency

0.8821

0.410

0.0810

Mixed Pathing

D2D Utility

0.9215

0.231

0.0624

>90% D2D Proxy

Conclusion: The D2D Utility policy achieved the best balance, reducing latency by ~50% compared to the Edge-heavy approach while maintaining high accuracy.

🛠️ Installation & Usage

Clone the repository:

git clone [https://github.com/yourusername/secure-offloading-simulator.git](https://github.com/yourusername/secure-offloading-simulator.git)
cd secure-offloading-simulator


Install dependencies:

pip install pandas numpy matplotlib


Run the simulation:

python offloading_simulator.py


🧠 Methodology

The simulator uses a Utility Function $U$ to rank paths:


$$U = w_1 \cdot Accuracy - w_2 \cdot Latency - w_3 \cdot Energy$$

Where $w_n$ are configurable weights. If the Security Module returns a Risk > Threshold, the system overrides the utility and forces Local NPU execution to prevent data leakage.

📜 License

Distributed under the MIT License.