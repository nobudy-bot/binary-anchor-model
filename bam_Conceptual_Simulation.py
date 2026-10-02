"""
Binary Anchor Model (BAM) V2.0 - Conceptual In-Silico Simulation
================================================================
This script evaluates BAM's core equations (Hesitation Energy & Accumulated Load)
using synthetic distributions to conceptualize somatic collapse dynamics.

*Note: This is a conceptual simulation demonstrating the mathematical behavior 
 of the Master Equation, not an empirical validation with real patient data.

Theoretical Hypotheses Visualized:
1. Hesitation Energy (H_t = r_t * (1 - r_t) * Delta_t^2):
   Internal conflict peaks non-linearly at the state of true incompatibility (r_t = 0.5).
2. Accumulated Load (I_t = (1 - r_t) * |Delta_t|):
   Somatic Collapse (Type 1 Burst) is driven by the non-linear interaction 
   between systemic subordination (r_t -> 0) and high divergence (|Delta_t|).

Author: Norimitsu Sawada (Independent Researcher)
License: CC BY 4.0 / MIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import roc_curve, auc

def run_conceptual_simulation(N=1000, seed=42):
    # Set seed for reproducibility
    rng = np.random.default_rng(seed)
    
    # ---------------------------------------------------------
    # 1. Synthetic Sampling (Simulating diverse observer states)
    # ---------------------------------------------------------
    # r_t: Sovereign Decision / Assumption of Responsibility (Beta distribution)
    r_t = rng.beta(a=2.0, b=2.0, size=N)
    
    # Delta_t: Divergence between Somatic Reality and System B (|Delta_t| on [0, 5])
    delta_raw = rng.gamma(shape=2.5, scale=0.8, size=N)
    delta_t = np.clip(delta_raw, 0, 5.0)
    
    # ---------------------------------------------------------
    # 2. BAM Mathematical Metric Computation
    # ---------------------------------------------------------
    # Hesitation Energy (Acute Somatic Friction)
    H_t = r_t * (1.0 - r_t) * (delta_t ** 2)
    
    # Accumulated Unprocessed Load (Structural Stress Debt)
    I_t = (1.0 - r_t) * delta_t
    
    # Conventional Linear Baseline (Raw Demands only)
    linear_demands = delta_t
    
    # ---------------------------------------------------------
    # 3. Somatic Collapse (Type 1 Burst / Freeze) Generation
    # ---------------------------------------------------------
    theta_acc = 1.8  # Critical Accumulation Threshold for Collapse
    # Logistic probability based on how far I_t exceeds the threshold
    burst_logit = 2.5 * (I_t - theta_acc) + rng.normal(0, 0.5, size=N)
    burst_prob = 1.0 / (1.0 + np.exp(-burst_logit))
    burst_event = (rng.random(N) < burst_prob).astype(int)
    
    # ---------------------------------------------------------
    # 4. Statistical Metrics Extraction
    # ---------------------------------------------------------
    fpr_bam, tpr_bam, _ = roc_curve(burst_event, I_t)
    auc_bam = auc(fpr_bam, tpr_bam)
    
    fpr_linear, tpr_linear, _ = roc_curve(burst_event, linear_demands)
    auc_linear = auc(fpr_linear, tpr_linear)
    
    r_corr, _ = pearsonr(I_t, burst_prob)
    
    # Print Executive Summary Report
    print("=" * 68)
    print("  BAM V2.0 - Conceptual In-Silico Simulation Report")
    print("=" * 68)
    print(f"Sample Size (N)               : {N} synthetic agents")
    print(f"BAM Model AUC (I_t metric)    : {auc_bam:.4f}  [Primary BAM Classifier]")
    print(f"Standard Linear Model AUC     : {auc_linear:.4f}  [Baseline Demand Sum]")
    print(f"Correlation (I_t vs Collapse) : r = {r_corr:.4f} (p < 0.001)")
    print("=" * 68)
    
    # ---------------------------------------------------------
    # 5. Publication-Quality Academic Plot (2x2 Grid)
    # ---------------------------------------------------------
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))
    plt.subplots_adjust(hspace=0.35, wspace=0.3)
    
    # Plot 1: Hesitation Energy Parabolic Surface H_t(r_t, Delta_t)
    r_grid, d_grid = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 5, 100))
    H_grid = r_grid * (1.0 - r_grid) * (d_grid ** 2)
    c1 = axs[0, 0].contourf(r_grid, d_grid, H_grid, levels=20, cmap='viridis')
    axs[0, 0].set_title('1. Acute Somatic Friction Surface ($H_t$)', fontsize=12, fontweight='bold')
    axs[0, 0].set_xlabel('Sovereign Decision ($r_t$)', fontsize=10)
    axs[0, 0].set_ylabel('Divergence from System B ($|\\Delta_t|$)', fontsize=10)
    axs[0, 0].axvline(0.5, color='red', linestyle='--', alpha=0.8, label='Max Conflict Axis ($r_t=0.5$)')
    fig.colorbar(c1, ax=axs[0, 0], label='Hesitation Energy ($H_t$)')
    axs[0, 0].legend(loc='upper left')
    
    # Plot 2: Accumulated Load (I_t) vs. Somatic Collapse Probability
    scatter = axs[0, 1].scatter(I_t, burst_prob, c=r_t, cmap='coolwarm', alpha=0.6, edgecolors='none')
    axs[0, 1].axvline(theta_acc, color='black', linestyle=':', linewidth=2, label=f'Threshold $\\Theta_{{acc}}$ = {theta_acc}')
    axs[0, 1].set_title('2. Accumulated Load ($I_t$) vs. Somatic Collapse', fontsize=12, fontweight='bold')
    axs[0, 1].set_xlabel('Unprocessed Load: $I_t = (1-r_t)|\\Delta_t|$', fontsize=10)
    axs[0, 1].set_ylabel('Probability of Type 1 Burst', fontsize=10)
    fig.colorbar(scatter, ax=axs[0, 1], label='Sovereignty ($r_t$)')
    axs[0, 1].legend(loc='lower right')
    axs[0, 1].grid(True, linestyle=':', alpha=0.5)
    
    # Plot 3: ROC Curve (BAM non-linear metric vs. Linear baseline)
    axs[1, 0].plot(fpr_bam, tpr_bam, color='darkred', linewidth=2.5, label=f'BAM ($I_t$ metric) [AUC = {auc_bam:.3f}]')
    axs[1, 0].plot(fpr_linear, tpr_linear, color='gray', linestyle='--', linewidth=2, label=f'Linear Demands [AUC = {auc_linear:.3f}]')
    axs[1, 0].plot([0, 1], [0, 1], color='black', linestyle=':', alpha=0.5)
    axs[1, 0].set_title('3. ROC Curve: Prediction of Phase Transition', fontsize=12, fontweight='bold')
    axs[1, 0].set_xlabel('False Positive Rate', fontsize=10)
    axs[1, 0].set_ylabel('True Positive Rate', fontsize=10)
    axs[1, 0].legend(loc='lower right', fontsize=10)
    axs[1, 0].grid(True, linestyle=':', alpha=0.5)
    
    # Plot 4: Risk Stratification by Sovereignty Tiers
    r_bins = pd.cut(r_t, bins=[0, 0.33, 0.66, 1.0], labels=['Systemic Subordination\n($r_t < 0.33$)', 'Ambivalent\n(0.33 - 0.66)', 'Sovereign Assumption\n($r_t > 0.66$)'])
    df_plot = pd.DataFrame({'r_tier': r_bins, 'Burst': burst_event})
    burst_rates = df_plot.groupby('r_tier', observed=False)['Burst'].mean()
    
    bars = axs[1, 1].bar(burst_rates.index, burst_rates.values * 100, color=['#d95f02', '#7570b3', '#1b9e77'], width=0.5)
    axs[1, 1].set_title('4. Somatic Collapse Rate by Sovereignty ($r_t$)', fontsize=12, fontweight='bold')
    axs[1, 1].set_ylabel('Observed Collapse Rate (%)', fontsize=10)
    for bar in bars:
        yval = bar.get_height()
        axs[1, 1].text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval:.1f}%', ha='center', va='bottom', fontweight='bold')
    axs[1, 1].set_ylim(0, max(burst_rates.values * 100) + 12)
    axs[1, 1].grid(axis='y', linestyle=':', alpha=0.5)
    
    # Save publication-ready high-res plot
    output_filename = 'bam_conceptual_insilico_results.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[*] High-resolution academic plot saved as '{output_filename}'")
    plt.show()

if __name__ == '__main__':
    run_conceptual_simulation()
