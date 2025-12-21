Secure Network-aware Offloading Simulator (SNOS)

🚀 Project Overview

This simulator models the decision-making process for task offloading in a heterogeneous mobile network (Mobile -> D2D Proxy -> Edge Cloud). It evaluates the trade-offs between Accuracy, Latency, and Energy Consumption while enforcing a Machine Learning-driven security layer.

Key Features

Multi-Path Offloading: Supports Local NPU, D2D Proxy, and Edge Cloud paths.

Security-Aware: Integrated risk-check module that triggers fallback to Local NPU upon threat detection.

Policy Comparison: Compares Max_Accuracy, Max_Latency, and D2D_Utility strategies.

Energy Modeling: Calculates Joule consumption based on transmission power and compute intensity.

📊 Experimental Results

Instead of traditional pathing, the simulator compared three major policy outcomes:

Max Accuracy Policy

Avg. Accuracy: 0.9434

Avg. Latency: 0.542s

Avg. Energy: 0.1250J

Trend: Heavily reliant on Edge Cloud.

Max Latency Policy

Avg. Accuracy: 0.8821

Avg. Latency: 0.410s

Avg. Energy: 0.0810J

Trend: Mixed pathing between Local and Edge.

D2D Utility Policy (Optimized)

Avg. Accuracy: 0.9215

Avg. Latency: 0.231s

Avg. Energy: 0.0624J

Trend: Over 90% of tasks routed through D2D Proxy.

Conclusion: The D2D Utility policy achieved the best balance, reducing latency by ~50% compared to the Edge-heavy approach while maintaining high accuracy.

🛠️ Installation & Usage

Clone the repository:

git clone [https://github.com/hunainaghai/secure-offloading-simulator.git](https://github.com/hunainaghai/secure-offloading-simulator.git)
cd secure-offloading-simulator


Install dependencies:

pip install pandas numpy


Run the simulation:

python offloading_simulator.py


🧠 Methodology

The simulator uses a Utility Function $U$ to rank paths:


$$U = w_1 \cdot Accuracy - w_2 \cdot Latency - w_3 \cdot Energy$$

Where $w_n$ are configurable weights. If the Security Module returns a Risk > Threshold, the system overrides the utility and forces Local NPU execution to prevent data leakage.

📜 License

Distributed under the MIT License.