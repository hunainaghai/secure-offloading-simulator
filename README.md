Secure Network-aware Offloading Simulator (SNOS)

A discrete-event simulator designed to evaluate security-aware offloading policies for Deep Learning (DL) video analytics in mobile edge environments.

Project Overview

Objective: Optimize the trade-off between inference accuracy, latency, and energy consumption.

Security Module: Implements a TFLite-based risk assessment that forces local NPU execution for high-risk tasks.

Network Tiers: Supports Local NPU, D2D (Peer-assisted), and Edge Cloud offloading.

Key Findings: The D2D Utility policy reduces cellular tail-energy by up to 40% compared to traditional cloud-only offloading.

Repository Structure

offloading_simulator.py: The core simulation engine built with SimPy.

TechnicalReport_SNOS.pdf: Full technical documentation and analysis.

README.md: Project summary and navigation guide.

How to Run

Ensure Python 3.8+ is installed.

Install dependencies: pip install simpy numpy tensorflow.

Run the simulator: python offloading_simulator.py.

