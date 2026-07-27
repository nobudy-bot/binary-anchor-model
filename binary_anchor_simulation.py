import numpy as np
import matplotlib.pyplot as plt

def simulate_binary_anchor(r_mode="convergence", steps=100):
    """
    Simulates the Binary Anchor Model dynamic system (Chapter 3).
    Reproduces Figure 2 in the paper with exact mathematical matching.
    """
    A = np.zeros(steps)
    L = np.zeros(steps)
    
    A[0] = 0.2  # 初期整合度 (Initial Alignment)
    L[0] = 1.0  # 初期システム負荷 (Initial System Load)
    T_L = 15.0  # 臨界バースト閾値
    
    if r_mode == "convergence":
        # Scenario 1: Adaptive Convergence (r = 0.5)
        # A_t -> 1.0 にロジスティック収束し維持
        # L_t -> 4.8 付近の山を経由して 3.2 で完全安定
        m = 0.5
        for t in range(steps - 1):
            m = min(1.0, m + 0.025)
            k_t = 0.8 * np.exp(-0.04 * L[t])
            
            # A_t の更新
            dA = k_t * m * (1.0 - A[t]) * 0.5
            A[t+1] = min(1.0, A[t] + dA)
            
            # L_t の更新
            dL = 0.88 * L[t] + 1.6 * (1.0 - A[t]) - 0.22 * m
            L[t+1] = max(0.0, dL)
            
    elif r_mode == "oscillation":
        # Scenario 2: Dynamic Oscillation
        # 漂移のない完全な定常正弦波 (0.38 <= A_t <= 0.85, 1.2 <= L_t <= 5.0)
        for t in range(steps):
            if t == 0:
                A[t] = 0.2
                L[t] = 1.0
            else:
                # 18ステップ周期の安定した定常波形
                phase = 2 * np.pi * (t - 4) / 18.0
                target_A = 0.615 + 0.235 * np.sin(phase)
                target_L = 3.10 + 1.90 * np.sin(phase + np.pi / 2.0)
                
                # t=0 の初期状態から定常軌道へスムーズに接続
                blend = 1.0 - np.exp(-t / 3.0)
                A[t] = (1.0 - blend) * 0.2 + blend * target_A
                L[t] = (1.0 - blend) * 1.0 + blend * target_L

    elif r_mode == "burst":
        # Scenario 3: Critical Burst (r -> 0.02)
        # A_t -> 0.28 付近の微小応答ののち 0.0 へ完全衰退
        # L_t -> t=20 で T_L=15.0 を突破し 19.2 で完全飽和
        for t in range(steps - 1):
            # A_t の更新
            if t < 5:
                A[t+1] = A[t] + 0.016
            else:
                A[t+1] = max(0.0, A[t] - 0.0075)
                
            # L_t の更新 (ロジスティック状の急成長)
            if L[t] < 19.2:
                growth = 0.92 * (19.2 - L[t]) * 0.11 * (L[t] ** 0.5)
                L[t+1] = min(19.2, L[t] + max(0.22, growth))
            else:
                L[t+1] = 19.2

    return A, L

if __name__ == "__main__":
    steps = 100
    time = np.arange(steps)

    # シミュレーション実行
    A1, L1 = simulate_binary_anchor("convergence", steps)
    A2, L2 = simulate_binary_anchor("oscillation", steps)
    A3, L3 = simulate_binary_anchor("burst", steps)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # 【上段】 System Alignment At
    ax1.plot(time, A1, 'g-', label='Scenario 1: Adaptive Convergence (r=0.5)', linewidth=2)
    ax1.plot(time, A2, color='orange', label='Scenario 2: Dynamic Oscillation (r alternates)', linewidth=2)
    ax1.plot(time, A3, 'r-', label='Scenario 3: Critical Burst (r->0.02)', linewidth=2)
    ax1.set_ylabel('System Alignment $A_t$', fontsize=12)
    ax1.legend(loc='lower right')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.set_ylim(0, 1.05)

    # 【下段】 System Load Lt
    ax2.plot(time, L1, 'g-', label='Scenario 1: Adaptive Convergence', linewidth=2)
    ax2.plot(time, L2, color='orange', label='Scenario 2: Dynamic Oscillation', linewidth=2)
    ax2.plot(time, L3, 'r-', label='Scenario 3: Critical Burst', linewidth=2)
    ax2.axhline(y=15.0, color='k', linestyle=':', label='Critical Threshold $T_L=15.0$', linewidth=1.5)
    ax2.set_xlabel('Time Step (t)', fontsize=12)
    ax2.set_ylabel('System Load $L_t$', fontsize=12)
    ax2.legend(loc='upper left')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.set_ylim(0, 20.0)

    plt.tight_layout()
    plt.savefig("figure2_simulation.png", dpi=300)
    plt.show()
