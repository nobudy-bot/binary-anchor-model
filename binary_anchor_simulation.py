import numpy as np
import matplotlib.pyplot as plt

def simulate_binary_anchor(r_mode="convergence", steps=100):
    """
    Simulates the Binary Anchor Model dynamic system (Chapter 3).
    
    Parameters:
        r_mode (str): 'convergence' (Scenario 1), 'oscillation' (Scenario 2), or 'burst' (Scenario 3).
        steps (int): Number of discrete time steps.
        
    Returns:
        A (ndarray): System Alignment over time.
        L (ndarray): System/Cognitive Load over time.
    """
    # 初期値の設定 (Initial Conditions)
    A = np.zeros(steps)
    L = np.zeros(steps)
    m = np.zeros(steps)
    
    A[0] = 0.2  # 初期整合度 (Initial Alignment)
    L[0] = 1.0  # 初期システム負荷 (Initial System Load)
    m[0] = 0.5  # 初期測定尺度 (Initial Measurement Metric)
    
    # 定数パラメータ (Model Parameters)
    k0 = 0.8
    lambda_param = 0.05
    alpha = 0.95
    beta = 1.2
    gamma = 0.8
    rho_r, kappa_r = 0.1, 1.0
    rho_s, kappa_s = 0.1, 1.0
    A_r_star, A_s_star = 1.0, 0.0
    T_L = 15.0  # 臨界バースト閾値 (Critical Burst Threshold)
    
    for t in range(steps - 1):
        # 責任配分パラメータ r の設定 (Scenario Routing)
        if r_mode == "convergence":
            r = 0.5  # Scenario 1: 適応的収束
        elif r_mode == "oscillation":
            r = 0.8 if (t // 10) % 2 == 0 else 0.2  # Scenario 2: 周期振動
        elif r_mode == "burst":
            r = 0.02  # Scenario 3: 外部システム依存極限 (r -> 0)
            
        # 関数論理の適用 (Explicit Functions)
        Phi_r = r ** 2
        Psi_rm = r * m[t]
        Omega_rule = 0.65 * m[t] * (1.0 - r)
        
        # 学習率の減衰 (Adaptive Learning Rate)
        k_t = k0 * np.exp(-lambda_param * L[t])
        if L[t] >= T_L:
            k_t = 0.0  # 臨界突破で学習フリーズ
            
        # 動態方程式の更新 (System Equations)
        dA = k_t * m[t] * (1.0 - A[t]) * Phi_r
        A[t+1] = np.clip(A[t] + dA, 0.0, 1.0)
        
        dL = alpha * L[t] + beta * (1.0 - A[t]) - gamma * Psi_rm + Omega_rule
        L[t+1] = max(0.0, dL)
        
        dm = rho_r * kappa_r * (A_r_star - A[t]) * r + rho_s * kappa_s * (A_s_star - A[t]) * (1.0 - r)
        m[t+1] = np.clip(m[t] + dm, 0.0, 1.0)
        
    return A, L

if __name__ == "__main__":
    # シミュレーション実行と描画 (Run and Plot)
    steps = 100
    time = np.arange(steps)

    A1, L1 = simulate_binary_anchor("convergence", steps)
    A2, L2 = simulate_binary_anchor("oscillation", steps)
    A3, L3 = simulate_binary_anchor("burst", steps)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # 整合度 At のグラフ
    ax1.plot(time, A1, 'g-', label='Scenario 1: Adaptive Convergence (r=0.5)', linewidth=2)
    ax1.plot(time, A2, color='orange', label='Scenario 2: Dynamic Oscillation (r alternates)', linewidth=2)
    ax1.plot(time, A3, 'r-', label='Scenario 3: Critical Burst (r->0.02)', linewidth=2)
    ax1.set_ylabel('System Alignment $A_t$', fontsize=12)
    ax1.legend(loc='lower right')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.set_ylim(0, 1.05)

    # システム負荷 Lt のグラフ
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
    
    # 画像の自動保存 (Auto-save Figure 2)
    plt.savefig("figure2_simulation.png", dpi=300)
    plt.show()
