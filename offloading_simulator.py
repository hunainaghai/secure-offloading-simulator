import numpy as np
import pandas as pd

# --- Simulator Configuration ---
class SecureOffloadingSim:
    def __init__(self):
        self.paths = {
            'Local_NPU': {'latency': 0.05, 'energy': 0.01, 'accuracy': 0.85, 'security': 1.0},
            'D2D_Proxy': {'latency': 0.15, 'energy': 0.04, 'accuracy': 0.92, 'security': 0.8},
            'Edge_Cloud': {'latency': 0.45, 'energy': 0.10, 'accuracy': 0.98, 'security': 0.7}
        }
    
    def calculate_utility(self, path, w_acc=0.5, w_lat=0.3, w_en=0.2):
        p = self.paths[path]
        # Utility = (Accuracy Weight) - (Latency Weight) - (Energy Weight)
        return (w_acc * p['accuracy']) - (w_lat * p['latency']) - (w_en * p['energy'])

    def run_simulation(self, policy='D2D_Utility', attack_detected=False):
        if attack_detected:
            return "Local_NPU", self.paths['Local_NPU']
        
        if policy == 'Max_Accuracy':
            path = 'Edge_Cloud'
        elif policy == 'Max_Latency':
            path = 'Local_NPU'
        else: # D2D_Utility
            utilities = {name: self.calculate_utility(name) for name in self.paths}
            path = max(utilities, key=utilities.get)
            
        return path, self.paths[path]

# --- Main Execution ---
if __name__ == "__main__":
    sim = SecureOffloadingSim()
    print("Running Secure Network-aware Offloading Simulator...")
    
    # Simulating the 'Winner' policy from your LinkedIn post
    decision, metrics = sim.run_simulation(policy='D2D_Utility')
    
    print(f"\nFinal Decision: {decision}")
    print(f"Metrics: Latency: {metrics['latency']}s, Accuracy: {metrics['accuracy']}, Energy: {metrics['energy']}J")