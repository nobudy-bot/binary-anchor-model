import matplotlib
matplotlib.use('Agg')  # Headless backend (Ensures 100% zero GUI error on any OS/server)
import matplotlib.pyplot as plt
import numpy as np

'''
Binary Anchor Model (BAM) V2.0 - Micro-Cognitive Engine
Official simulation script for "The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure"
Author: Norimitsu Sawada (Independent Researcher)
Repository: https://github.com/nobudy-bot/binary-anchor-model
Description: A strict translation of the V2.0 Master Equation (Level 0-3 architecture)
demonstrating the phase transition from Somatic Friction to Systemic Breakdown.
'''

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def run_simulation(T=200, eta_A0=0.10, seed=42):
    np.random.seed(seed)
    t = np.arange(T)
    
    # m_sys: System B Demand (Social Anchor / Institutional Pressure)
    m_sys = np.full(T, 0.8)
    m_sys[120:] = 0.3  # Step-shift in social expectation (System B disruption) at t=120
    
    # BAM Parameters
    w_s = 2.0
    w_delta = 4.0
    theta_bias = 2.0
    gamma = 0.02       # Metabolic load dissipation
    T_E = 0.5          # WTA Excitation Threshold
    H_max = 0.15       # Type 2 Burst Threshold (Acute Somatic Violence)
    Theta_acc = 5.0    # Type 1 Burst Threshold (Somatic Collapse / Freeze)
    
    # Initialization
    m_t = 0.5          # Biological Needs / Felt Sense (System A baseline)
    I_current = 0.0    # Accumulated Unprocessed Load (Structural Debt)
    
    history = {'t': t, 'm_t': [], 'm_sys': m_sys, 'V_t': [], 'r_t': [], 'H_t': [], 'I_t': [], 'A_t': []}
    bursts = []
    
    for i in range(T):
        # 1. Divergence calculation
        delta_t = m_t - m_sys[i]
        abs_delta = abs(delta_t)
        
        # 2. Survival Urgency (s_t) & Sovereign Assumption (r_t) [Eq. 20]
        s_t = np.clip(abs_delta * 1.5, 0, 1)
        r_t = sigmoid(w_s * s_t + w_delta * abs_delta - theta_bias)
        
        # 3. Master Equation Integration [Eq. 5]
        v_t = r_t * m_t + (1 - r_t) * m_sys[i]
        
        # 4. WTA Decision Logic [Eq. 4 & 6]
        a_t = 1 if v_t > T_E else 0
        
        # 5. Cognitive Loads [Eq. 21 & 29]
        H_t = r_t * (1 - r_t) * (delta_t ** 2)  # Acute Somatic Friction
        I_current = (1 - gamma) * I_current + (1 - r_t) * abs_delta # Chronic Load
        
        # 6. Phase Transition (Burst / Somatic Collapse) [Eq. 24 & 25]
        if H_t > H_max:
            bursts.append((i, 'Type 2'))
            H_t, I_current = 0, 0 # Heat dissipation
        elif I_current > Theta_acc:
            bursts.append((i, 'Type 1'))
            I_current = I_current * 0.1 # 90% Discharge/Freeze reset
            
        # 7. System A Auto-correction (Metabolic Update) [Eq. 19 & 14]
        # High eta_A0 allows m_t to adapt and shrink delta_t, low eta_A0 causes accumulation
        m_t = np.clip(m_t - eta_A0 * r_t * delta_t, 0, 1)
        
        # Record state
        history['m_t'].append(m_t)
        history['V_t'].append(v_t)
        history['r_t'].append(r_t)
        history['H_t'].append(H_t)
        history['I_t'].append(I_current)
        history['A_t'].append(a_t)
        
    return history, bursts

def plot_results(data, bursts, filename='bam_simulation_result.png'):
    # Standard matplotlib with clean academic grid aesthetics
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    for ax in [ax1, ax2]:
        ax.grid(True, color='#E0E0E0', linestyle='-', linewidth=0.5)
        ax.set_facecolor('#FAFAFA')
        for spine in ax.spines.values():
            spine.set_color('#BBBBBB')
    
    # Plot 1: Components of the Master Equation
    ax1.plot(data['t'], data['m_t'], label=r'Somatic Reality ($m_t$)', color='green', alpha=0.8)
    ax1.plot(data['t'], data['m_sys'], label=r'System B Demand ($m_{\mathrm{sys}}$)', color='blue', linestyle='--')
    ax1.plot(data['t'], data['V_t'], label=r'Integrated Input ($V_t$)', color='black', linewidth=2)
    ax1.axhline(0.5, color='red', linestyle=':', label=r'WTA Threshold ($T_{\mathrm{E}}$)')
    ax1.set_title("BAM V2.0: Master Equation & Somatic Adaptation", fontsize=14, fontweight='bold')
    ax1.set_ylabel("Metric State Space")
    ax1.legend(loc='upper right')
    
    # Plot 2: Unprocessed Load and Somatic Collapse
    ax2.plot(data['t'], data['I_t'], label=r'Accumulated Load ($I_t$)', color='orange', linewidth=2)
    ax2.axhline(5.0, color='darkred', linestyle='--', label=r'Collapse Threshold ($\Theta_{\mathrm{acc}}$)')
    
    for b_time, b_type in bursts:
        color = 'red' if 'Type 2' in b_type else 'black'
        ax2.axvline(b_time, color=color, alpha=0.5, linestyle='-')
        
    ax2.set_title("BAM V2.0: Structural Stress Debt & Somatic Collapse", fontsize=14, fontweight='bold')
    ax2.set_xlabel("Timestep ($t$)")
    ax2.set_ylabel("Accumulated Load ($I_t$)")
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"[*] Plot successfully saved as {filename}")

if __name__ == "__main__":
    print("[*] Running BAM V2.0 Core simulations...")
    data_res, b_res = run_simulation(eta_A0=0.10) # Resilient profile
    data_vul, b_vul = run_simulation(eta_A0=0.02) # Vulnerable profile
    
    # Generate individual dynamics plot
    plot_results(data_vul, b_vul, 'bam_simulation_vulnerable.png')
    
    # Generate Comparison Plot (Figure 5 in paper)
    plt.figure(figsize=(10, 6))
    plt.grid(True, color='#E0E0E0', linestyle='-', linewidth=0.5)
    plt.gca().set_facecolor('#FAFAFA')
    
    plt.plot(data_vul['t'], data_vul['I_t'], 'r', label=r'Vulnerable Profile (Low Amygdala Plasticity: $\eta_{A0} = 0.02$)', linewidth=2)
    plt.plot(data_res['t'], data_res['I_t'], 'b', label=r'Resilient Profile (High Amygdala Plasticity: $\eta_{A0} = 0.10$)', linewidth=2)
    plt.axhline(5.0, color='black', linestyle='--', label=r'Collapse Threshold ($\Theta_{acc} = 5.0$)')
    plt.title(r"BAM: Impact of Amygdala Plasticity ($\eta_{A0}$) on Somatic Collapse", fontsize=13, fontweight='bold')
    plt.xlabel("Timestep ($t$)")
    plt.ylabel("Accumulated Unprocessed Load ($I_t$)")
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('bam_comparison_eta.png', dpi=300)
    plt.close()
    print("[*] Comparison plot successfully saved as bam_comparison_eta.png")
    print("[*] All BAM Core Engine tasks completed successfully.")
