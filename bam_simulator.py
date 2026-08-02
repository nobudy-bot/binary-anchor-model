
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

'''
Binary Anchor Model (BAM) - Numerical Simulation
This script simulates the Master Equation A_t = WTA(V_t) and 
the accumulation of Hesitation Energy H_t based on Amygdala Plasticity (eta_A0).
'''

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def run_simulation(T=200, eta_A0=0.05, theta=10.0, seed=42):
    np.random.seed(seed)
    t = np.arange(T)
    
    # m_t: Biological needs (System A signals)
    m_t = 0.5 + 0.3 * np.sin(2 * np.pi * t / 60) + np.random.normal(0, 0.02, T)
    
    # m_sys: Social life maintenance (System B signals)
    m_sys = np.full(T, 0.8)
    m_sys[120:] = 0.3 # Shift in social expectation at t=120
    
    # Initialization
    H = np.zeros(T)
    A = np.zeros(T)
    V = np.zeros(T)
    r = np.zeros(T)
    bursts = []
    
    h_current = 0
    for i in range(T):
        # r_t: Responsibility allocation (tension parameter)
        r_val = 0.7 + 0.2 * np.cos(2 * np.pi * i / 100)
        r[i] = r_val
        
        # Master Equation: V_t = r*m + (1-r)*m_sys
        v_val = r_val * m_t[i] + (1 - r_val) * m_sys[i]
        V[i] = v_val
        
        # WTA Decision
        A[i] = 1 if v_val > 0.5 else 0
        
        # Hesitation Energy (H_t) calculation
        # delta_t: Divergence between System A and System B
        delta = abs(m_t[i] - m_sys[i])
        
        # H_t accumulation logic with recovery (eta_A0)
        h_current = max(0, h_current + r_val * delta - eta_A0)
        
        # Burst event (Threshold theta)
        if h_current > theta:
            bursts.append(i)
            h_current = h_current * 0.1 # Partial discharge after burst
            
        H[i] = h_current
        
    return pd.DataFrame({'t': t, 'm_t': m_t, 'm_sys': m_sys, 'V_t': V, 'H_t': H, 'A_t': A}), bursts

def plot_results(df, bursts, filename='bam_simulation_result.png'):
    sns.set_theme(style="whitegrid")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    # Plot 1: Components of the Master Equation
    ax1.plot(df['t'], df['m_t'], label='Bio Need (m_t)', color='green', alpha=0.5)
    ax1.plot(df['t'], df['m_sys'], label='Social Demand (m_sys)', color='blue', linestyle='--')
    ax1.plot(df['t'], df['V_t'], label='WTA Argument (V_t)', color='black', linewidth=2)
    ax1.axhline(0.5, color='red', linestyle=':', label='WTA Threshold')
    ax1.set_title("BAM V2.4: Master Equation Dynamics")
    ax1.legend(loc='upper right')
    
    # Plot 2: Hesitation Energy and Bursts
    ax2.plot(df['t'], df['H_t'], label='Hesitation Energy (H_t)', color='purple')
    ax2.axhline(10.0, color='darkred', linestyle='--', label='Burst Threshold (theta)')
    for b in bursts:
        ax2.axvline(b, color='orange', alpha=0.3)
    ax2.set_title("BAM V2.4: Hesitation Energy Accumulation")
    ax2.set_xlabel("Time (t)")
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Plot saved as {filename}")

if __name__ == "__main__":
    # Simulate Resilient (High eta_A0) vs Vulnerable (Low eta_A0)
    print("Running BAM simulations...")
    df_res, b_res = run_simulation(eta_A0=0.10)
    df_vul, b_vul = run_simulation(eta_A0=0.02)
    
    plot_results(df_vul, b_vul, 'bam_simulation_vulnerable.png')
    
    # Comparison Plot
    plt.figure(figsize=(10, 6))
    plt.plot(df_vul['t'], df_vul['H_t'], 'r', label='Vulnerable (Low eta_A0)')
    plt.plot(df_res['t'], df_res['H_t'], 'b', label='Resilient (High eta_A0)')
    plt.axhline(10.0, color='black', linestyle='--', label='Burst Threshold')
    plt.title("BAM: Impact of Amygdala Plasticity (eta_A0) on Energy Accumulation")
    plt.xlabel("Time (t)")
    plt.ylabel("Hesitation Energy (H_t)")
    plt.legend()
    plt.savefig('bam_comparison_eta.png')
    print("Comparison plot saved.")
