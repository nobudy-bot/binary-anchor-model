import matplotlib
matplotlib.use('Agg')  # Headless backend (Ensures zero GUI error on any OS/server)
import matplotlib.pyplot as plt
import numpy as np

'''
Binary Anchor Model (BAM) - V1.0 Dynamical Simulation
Official reproduction script for Figure 2 in "The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure (V1.0)"
Author: Norimitsu Sawada (ORCID: 0009-0001-3306-0048)
Repository: https://github.com/nobudy-bot/binary-anchor-model
Dependencies: ONLY numpy and matplotlib
'''

def simulate_v1_scenario(scenario_type, T=100, seed=42):
    np.random.seed(seed)
    
    # Base parameters matching V1 Chapter 3.4
    k0 = 0.8
    lam = 0.15
    alpha = 0.85
    beta = 1.2
    gamma = 0.9
    eta = 0.05
    TL_threshold = 15.0
    
    # State variable arrays
    A = np.zeros(T)
    L = np.zeros(T)
    m = np.zeros(T)
    
    # Initial conditions
    A[0] = 0.2
    L[0] = 2.0
    m[0] = 0.5
    
    # Target preferences for ruler updating
    Ar_star = 0.9
    As_star = 0.8
    rho_r, kappa_r = 0.2, 0.5
    rho_s, kappa_s = 0.2, 0.5
    
    for t in range(T - 1):
        # Scenario-dependent responsibility allocation r
        if scenario_type == 'convergence':
            r = 0.5  # Shared responsibility
        elif scenario_type == 'oscillation':
            r = 0.5 + 0.4 * np.sin(2 * np.pi * t / 20)  # Oscillating responsibility
        elif scenario_type == 'burst':
            r = 0.02  # Extreme system dependency (r -> 0)
        else:
            r = 0.5
            
        # 1. k_t: Learning rate with exponential load decay
        k_t = k0 * np.exp(-lam * L[t])
        
        # 2. Phi(r): Non-linear influence of r (Phi(r) = r^2)
        phi_r = r ** 2
        
        # Environmental stochastic noise
        eps_t = np.random.normal(0, 0.1)
        
        # 3. A_{t+1}: System Alignment update
        A_next = A[t] + k_t * m[t] * (1.0 - A[t]) * phi_r - eta * eps_t
        A[t + 1] = np.clip(A_next, 0.0, 1.0)
        
        # 4. Metabolic load dissipation Psi(r, m) and Rule Overhead Omega_rule
        psi_val = r * m[t]
        omega_rule = 0.65 * m[t] * (1.0 - r) * (1.0 + 0.05 * t)  # Accumulating rule overhead
        
        # 5. L_{t+1}: Cumulative System Load update
        L_next = alpha * L[t] + beta * (1.0 - A[t]) - gamma * psi_val + omega_rule
        L[t + 1] = max(0.0, L_next)
        
        # 6. m_{t+1}: Internal Ruler adaptation
        m_update = (m[t] 
                    + rho_r * kappa_r * (Ar_star - A[t]) * r 
                    + rho_s * kappa_s * (As_star - A[t]) * (1.0 - r))
        m[t + 1] = np.clip(m_update, 0.0, 1.0)
        
    return A, L

def plot_v1_figure2(filename='bam_v1_simulation.png'):
    T = 100
    timesteps = np.arange(T)
    
    # Run 3 distinct dynamic scenarios
    A_conv, L_conv = simulate_v1_scenario('convergence', T=T)
    A_osc, L_osc = simulate_v1_scenario('oscillation', T=T)
    A_burst, L_burst = simulate_v1_scenario('burst', T=T)
    
    # Create Figure 2 style plot (2 subplots)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    for ax in [ax1, ax2]:
        ax.grid(True, color='#E0E0E0', linestyle='-', linewidth=0.5)
        ax.set_facecolor('#FAFAFA')
        for spine in ax.spines.values():
            spine.set_color('#BBBBBB')
            
    # Subplot 1: System Alignment A_t (Agreement)
    ax1.plot(timesteps, A_conv, color='green', linewidth=2, label='Scenario 1: Adaptive Convergence ($r = 0.5$)')
    ax1.plot(timesteps, A_osc, color='orange', linewidth=2, label='Scenario 2: Dynamic Oscillation ($r$ alternates)')
    ax1.plot(timesteps, A_burst, color='darkred', linewidth=2, label='Scenario 3: Critical Burst ($r \\to 0.02$)')
    ax1.set_title("Simulation Scenarios: Alignment and System Load Dynamics (V1.0)", fontsize=13, fontweight='bold')
    ax1.set_ylabel("System Alignment $A_t$ (Agreement)", fontsize=11)
    ax1.set_ylim(-0.05, 1.05)
    ax1.legend(loc='lower right', fontsize=9)
    
    # Subplot 2: System Load L_t (Cognitive / System Load)
    ax2.plot(timesteps, L_conv, color='green', linewidth=2, label='Scenario 1: Adaptive Convergence')
    ax2.plot(timesteps, L_osc, color='orange', linewidth=2, label='Scenario 2: Dynamic Oscillation')
    ax2.plot(timesteps, L_burst, color='darkred', linewidth=2, label='Scenario 3: Critical Burst ($r \\to 0.02$)')
    ax2.axhline(15.0, color='darkred', linestyle=':', linewidth=1.5, label='Critical Threshold $T_L = 15.0$')
    ax2.set_xlabel("Time Step ($t$)", fontsize=11)
    ax2.set_ylabel("System Load $L_t$ (Cognitive/System Load)", fontsize=11)
    ax2.set_ylim(-0.5, 21.0)
    ax2.legend(loc='upper left', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"[*] V1 Simulation plot successfully saved as {filename}")

if __name__ == "__main__":
    print("[*] Running BAM V1.0 System Dynamics Simulation...")
    plot_v1_figure2()
    print("[*] V1 Figure 2 reproduction completed successfully.")
