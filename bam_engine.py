import matplotlib
matplotlib.use('Agg')  # Headless backend (Ensures 100% zero GUI error on any OS/server)
import matplotlib.pyplot as plt
import numpy as np

'''
Binary Anchor Model (BAM) - Numerical Simulation V1.0
Official simulation script for "The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure"
Author: Norimitsu Sawada (ORCID: 0009-0001-3306-0048)
Repository: https://github.com/nobudy-bot/binary-anchor-model
Dependencies: ONLY numpy and matplotlib (Maximum portability, zero-friction execution)
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
    m_sys[120:] = 0.3  # Step-shift in social expectation at t=120
    
    # Initialization
    H = np.zeros(T)
    A = np.zeros(T)
    V = np.zeros(T)
    r = np.zeros(T)
    bursts = []
    
    h_current = 0.0
    for i in range(T):
        # r_t: Responsibility allocation (tension parameter)
        r_val = 0.7 + 0.2 * np.cos(2 * np.pi * i / 100)
        r[i] = r_val
        
        # Master Equation: V_t = r*m + (1-r)*m_sys
        v_val = r_val * m_t[i] + (1 - r_val) * m_sys[i]
        V[i] = v_val
        
        # WTA Decision (Binary Execution: A_t in {0, 1})
        A[i] = 1 if v_val > 0.5 else 0
        
        # Divergence delta_t
        delta = abs(m_t[i] - m_sys[i])
        
        # Hesitation Energy (H_t) accumulation with basal amygdala recovery (eta_A0)
        h_current = max(0.0, h_current + r_val * delta - eta_A0)
        
        # Burst event (Threshold theta exceedance -> Phase transition discharge)
        if h_current > theta:
            bursts.append(i)
            h_current = h_current * 0.1  # 90% discharge reset
            
        H[i] = h_current
        
    # Return as standard dictionary (Pure python, zero pandas dependency)
    return {'t': t, 'm_t': m_t, 'm_sys': m_sys, 'V_t': V, 'H_t': H, 'A_t': A}, bursts

def plot_results(data, bursts, filename='bam_simulation_result.png'):
    # Standard matplotlib with clean academic grid aesthetics
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    for ax in [ax1, ax2]:
        ax.grid(True, color='#E0E0E0', linestyle='-', linewidth=0.5)
        ax.set_facecolor('#FAFAFA')
        for spine in ax.spines.values():
            spine.set_color('#BBBBBB')
    
    # Plot 1: Components of the Master Equation
    ax1.plot(data['t'], data['m_t'], label=r'Biological Needs ($m_t$)', color='green', alpha=0.6)
    ax1.plot(data['t'], data['m_sys'], label=r'Social Demands ($m_{\mathrm{sys}}$)', color='blue', linestyle='--')
    ax1.plot(data['t'], data['V_t'], label=r'Integrated Input ($V_t$)', color='black', linewidth=2)
    ax1.axhline(0.5, color='red', linestyle=':', label=r'WTA Threshold ($T_{\mathrm{E}}$)')
    ax1.set_title("BAM V2.0: Master Equation Dynamics", fontsize=14, fontweight='bold')
    ax1.set_ylabel("Metric State Space")
    ax1.legend(loc='upper right')
    
    # Plot 2: Hesitation Energy and Bursts
    ax2.plot(data['t'], data['H_t'], label=r'Hesitation Energy ($H_t$)', color='purple', linewidth=2)
    ax2.axhline(10.0, color='darkred', linestyle='--', label=r'Burst Threshold ($\Theta_{\mathrm{burst}}$)')
    for b in bursts:
        ax2.axvline(b, color='orange', alpha=0.4, linestyle='-')
    ax2.set_title("BAM V2.0: Hesitation Energy Accumulation & Burst Discharge", fontsize=14, fontweight='bold')
    ax2.set_xlabel("Timestep ($t$)")
    ax2.set_ylabel("Cognitive Friction ($H_t$)")
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"[*] Plot successfully saved as {filename}")

if __name__ == "__main__":
    print("[*] Running BAM simulations...")
    data_res, b_res = run_simulation(eta_A0=0.10)
    data_vul, b_vul = run_simulation(eta_A0=0.02)
    
    # Generate individual dynamics plot
    plot_results(data_vul, b_vul, 'bam_simulation_vulnerable.png')
    
    # Generate Comparison Plot (Figure 5 in paper)
    plt.figure(figsize=(10, 6))
    plt.grid(True, color='#E0E0E0', linestyle='-', linewidth=0.5)
    plt.gca().set_facecolor('#FAFAFA')
    
    plt.plot(data_vul['t'], data_vul['H_t'], 'r', label=r'Vulnerable Profile (Low $\eta_{A0} = 0.02$)', linewidth=2)
    plt.plot(data_res['t'], data_res['H_t'], 'b', label=r'Resilient Profile (High $\eta_{A0} = 0.10$)', linewidth=2)
    plt.axhline(10.0, color='black', linestyle='--', label=r'Burst Threshold ($\Theta = 10.0$)')
    plt.title(r"BAM: Impact of Amygdala Plasticity ($\eta_{A0}$) on Energy Accumulation", fontsize=13, fontweight='bold')
    plt.xlabel("Timestep ($t$)")
    plt.ylabel("Hesitation Energy ($H_t$)")
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('bam_comparison_eta.png', dpi=300)
    plt.close()
    print("[*] Comparison plot successfully saved as bam_comparison_eta.png")
    print("[*] All BAM simulation tasks completed successfully.")
