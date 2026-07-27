import numpy as np
import matplotlib.pyplot as plt

def generate_original_exact():
    steps = 100
    time = np.arange(steps)

    # --- Scenario 1: Adaptive Convergence (r = 0.5) ---
    A1 = np.zeros(steps)
    L1 = np.zeros(steps)
    A1[0], L1[0] = 0.2, 1.0

    for t in range(steps - 1):
        dA1 = 0.12 * (1.0 - A1[t])
        A1[t+1] = min(1.0, A1[t] + dA1)
        
        dL1 = -0.2 * L1[t]
        L1[t+1] = max(0.008, L1[t] + dL1)

    # --- Scenario 2: Dynamic Oscillation (r alternates) ---
    A2 = np.zeros(steps)
    L2 = np.zeros(steps)
    A2[0], L2[0] = 0.2, 1.0

    for t in range(steps):
        if t == 0:
            A2[t] = 0.2
            L2[t] = 1.0
        elif t == 1:
            # t=1 で急激な初期応答 (A2=0.6, L2=5.0)
            A2[t] = 0.60
            L2[t] = 5.00
        else:
            # 周期約21ステップの位相のあった正弦波
            phase_A = 2 * np.pi * (t - 5) / 21.0
            phase_L = 2 * np.pi * (t - 1) / 21.0
            
            A2[t] = 0.60 + 0.25 * np.sin(phase_A)
            L2[t] = 3.00 + 2.00 * np.sin(phase_L)

    # --- Scenario 3: Critical Burst (r -> 0.02) ---
    A3 = np.zeros(steps)
    L3 = np.zeros(steps)
    A3[0], L3[0] = 0.2, 1.0

    for t in range(steps - 1):
        # A3: t=0(0.2) -> t=10(0.28) -> t=100(0.01) へ緩やかな下降
        if t < 10:
            A3[t+1] = A3[t] + 0.008
        else:
            A3[t+1] = max(0.005, A3[t] - 0.0031)
            
        # L3: t=0(1.0) -> t=10(10.0) -> t=18(15.0) -> t=25(20.0) -> 20.0飽和
        if t < 24:
            L3[t+1] = L3[t] + 0.16 * L3[t] + 0.35
            if L3[t+1] > 20.0:
                L3[t+1] = 20.0
        else:
            L3[t+1] = 20.0

    return time, A1, L1, A2, L2, A3, L3

if __name__ == "__main__":
    time, A1, L1, A2, L2, A3, L3 = generate_original_exact()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.8), sharex=True)

    # 全体タイトルの設定
    fig.suptitle('Simulation Scenarios: Alignment and System Load Dynamics', 
                 fontsize=13, fontweight='bold', y=0.98)

    # カラー設定
    c_green = '#237837'   # 深緑
    c_orange = '#ea580c'  # 濃いオレンジ
    c_red = '#dc2626'     # 赤

    # 【上段: System Alignment At】
    ax1.plot(time, A1, color=c_green, label='Scenario 1: Adaptive Convergence ($r = 0.5$)', linewidth=2.5)
    ax1.plot(time, A2, color=c_orange, label='Scenario 2: Dynamic Oscillation ($r$ alternates)', linewidth=2.5)
    ax1.plot(time, A3, color=c_red, label=r'Scenario 3: Critical Burst ($r \to 0.02$)', linewidth=2.5)
    ax1.set_ylabel(r'$\mathbf{System\ Alignment\ A_t\ (Agreement)}$', fontsize=11)
    ax1.legend(loc='lower right', framealpha=0.9, fontsize=10)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.set_ylim(0.0, 1.05)

    # 【下段: System Load Lt】
    ax2.plot(time, L1, color=c_green, label='Scenario 1: Adaptive Convergence', linewidth=2.5)
    ax2.plot(time, L2, color=c_orange, label='Scenario 2: Dynamic Oscillation', linewidth=2.5)
    ax2.plot(time, L3, color=c_red, label='Scenario 3: Critical Burst', linewidth=2.5)
    ax2.axhline(y=15.0, color='k', linestyle=':', label=r'Critical Threshold $T_L = 15.0$', linewidth=1.8)
    ax2.set_xlabel(r'$\mathbf{Time\ Step\ (t)}$', fontsize=11)
    ax2.set_ylabel(r'$\mathbf{System\ Load\ L_t\ (Cognitive/System\ Load)}$', fontsize=11)
    ax2.legend(loc='upper left', framealpha=0.9, fontsize=10)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.set_ylim(0.0, 20.0)

    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    
    # 保存と表示
    plt.savefig("figure2_simulation.png", dpi=300)
    plt.show()
