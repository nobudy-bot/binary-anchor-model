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

def show_results(data_vul, b_vul, data_res, b_res):
    # --- Figure 1: Individual Dynamics (Vulnerable Profile) ---
    fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    for ax in [ax1, ax2]:
        ax.grid(True, color='#E0E0E0', linestyle='-', linewidth=0.5)
        ax.set_facecolor('#FAFAFA')
    
    ax1.plot(data_vul['t'], data_vul['m_t'], label=r'Somatic Reality ($m_t$)', color='green', alpha=0.8)
    ax1.plot(data_vul['t'], data_vul['m_sys'], label=r'System B Demand ($m_{\mathrm{sys}}$)', color='blue', linestyle='--')
    ax1.plot(data_vul['t'], data_vul['V_t'], label=r'Integrated Input ($V_t$)', color='black', linewidth=2)
    ax1.axhline(0.5, color='red', linestyle=':', label=r'WTA Threshold ($T_{\mathrm{E}}$)')
    ax1.set_title("Master Equation & Somatic Adaptation", fontsize=12, fontweight='bold')
    ax1.set_ylabel("Metric State Space")
    ax1.legend(loc='upper right')
    
    ax2.plot(data_vul['t'], data_vul['I_t'], label=r'Accumulated Load ($I_t$)', color='orange', linewidth=2)
    ax2.axhline(5.0, color='darkred', linestyle='--', label=r'Collapse Threshold ($\Theta_{\mathrm{acc}}$)')
    
    for b_time, b_type in b_vul:
        color = 'red' if 'Type 2' in b_type else 'black'
        ax2.axvline(b_time, color=color, alpha=0.5, linestyle='-')
        
    ax2.set_title("Structural Stress Debt & Somatic Collapse", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Timestep ($t$)")
    ax2.set_ylabel("Accumulated Load ($I_t$)")
    ax2.legend(loc='upper right')
    
    fig1.tight_layout()
    plt.show() # 明示的にここで1枚目を描画

    # --- Figure 2: Comparison Plot (Vulnerable vs Resilient) ---
    fig2, ax3 = plt.subplots(figsize=(10, 6))
    ax3.grid(True, color='#E0E0E0', linestyle='-', linewidth=0.5)
    ax3.set_facecolor('#FAFAFA')
    
    ax3.plot(data_vul['t'], data_vul['I_t'], 'r', label=r'Vulnerable Profile (Low Plasticity: $\eta_{A0} = 0.02$)', linewidth=2)
    ax3.plot(data_res['t'], data_res['I_t'], 'b', label=r'Resilient Profile (High Plasticity: $\eta_{A0} = 0.10$)', linewidth=2)
    ax3.axhline(5.0, color='black', linestyle='--', label=r'Collapse Threshold ($\Theta_{acc} = 5.0$)')
    ax3.set_title(r"Impact of Amygdala Plasticity ($\eta_{A0}$) on Somatic Collapse", fontsize=13, fontweight='bold')
    ax3.set_xlabel("Timestep ($t$)")
    ax3.set_ylabel("Accumulated Unprocessed Load ($I_t$)")
    ax3.legend(loc='upper left')
    
    fig2.tight_layout()
    plt.show() # 明示的にここで2枚目を描画

if __name__ == "__main__":
    print("[*] Running BAM V2.0 Core simulations...")
    data_res, b_res = run_simulation(eta_A0=0.10) # Resilient profile
    data_vul, b_vul = run_simulation(eta_A0=0.02) # Vulnerable profile
    
    print("[*] Displaying BAM simulation results...")
    show_results(data_vul, b_vul, data_res, b_res)
    print("[*] Simulation completed.")
