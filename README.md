# Binary Anchor Model (BAM) V2.0

[ **English** | [日本語](README_JA.md) ]

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21759689.svg)](https://doi.org/10.5281/zenodo.21759689)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This repository contains the official Python simulation code for the paper:  
**"The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure"** by **Norimitsu Sawada**.

- **Zenodo Preprint (V2.0.0):** [DOI: 10.5281/zenodo.21759689](https://doi.org/10.5281/zenodo.21759689)
- **Concept DOI (All Versions):** [DOI: 10.5281/zenodo.21566423](https://doi.org/10.5281/zenodo.21566423)
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 🚀 How to Run

Clone the repository and install minimal dependencies:

```bash
# 1. Clone repository
git clone https://github.com/nobudy-bot/binary-anchor-model.git
cd binary-anchor-model

# 2. Install minimal dependencies
pip install -r requirements.txt
```

### Simulation Options:

- **Option A: Micro-Cognitive Engine (V2.0 Core / Recommended)**  
  Runs the high-resolution simulation of the Master Equation $A_t = \mathrm{WTA}(V_t)$. Focuses on individual brain dynamics (Amygdala vs. PFC):
  ```bash
  python bam_engine.py
  ```

- **Option B: Original Paper Baseline (V2.0)**  
  The original baseline script used to generate figures in the V2.0 preprint:
  ```bash
  python bam_simulator.py
  ```

- **Option C: Macro-Social Dynamics (V1.0 Legacy)**  
  Simulates the inter-observer interaction loop, demonstrating institutional fossilization and system-wide "Critical Burst":
  ```bash
  python legacy_simulations/bam_v1_macro_dynamics.py
  ```

### Outputs Generated:
- **V2.0 Output:** `bam_simulation_vulnerable.png`, `bam_comparison_eta.png` (Individual cognitive collapse/recovery matching Section 8).
- **V1.0 Output:** `bam_v1_simulation.png` (Reproduction of Figure 2 from V1 paper: Convergence, Oscillation, and Burst scenarios).

---

## 🧠 Multiscale Architecture

The **Binary Anchor Model (BAM)** is a fractal theoretical framework that describes the same structural trap across different scales:

| Scale | Model Version | Focus | Core Mechanism |
| :--- | :--- | :--- | :--- |
| **Micro (Brain)** | **V2.0 (Core)** | Individual Decision-making | WTA Master Equation / Amygdala-PFC Antagonism |
| **Macro (Society)** | **V1.0 (Legacy)** | Institutional Saturation | Recursive Update Loops / Fossilized Knowledge |

- **System A (Biological Anchor):** Rooted in survival, interoception, and the amygdala.
- **System B (Social Anchor):** Rooted in language, institutions, and the PFC.

---

## 🛠 Master Equation (V2.0)

Version 2.0 formalizes the Master Equation as the apex organizing principle of the framework:

$$A_t = \mathrm{WTA}(V_t) \in \{0, 1\}$$
$$V_t = r_t \cdot m_t + (1 - r_t) \cdot m_{\mathrm{sys}, t}$$
$$\mathrm{WTA}(V_t) = \theta(V_t - T_{\mathrm{E}})$$

### Key Formalizations:
- **Probabilistic Extension (Soft-WTA):** $A_t \sim \mathrm{Bernoulli}(\sigma(V_t - T_{\mathrm{E}}))$
- **Hesitation Energy ($H_t$) & Accumulated Load ($I_t$):** Dual-trigger mechanisms for computational breakdown (Burst).
- **Neurobiological Grounding of $\eta_{A0}$:** Amygdala sensitivity and plasticity ($\eta_{\mathrm{A}}(t) = \eta_{A0} \cdot (1 - \phi_t)$).
- **Recovery & Threshold Modification:** Quantification of $T_{\mathrm{recovery}}$ and past violence history ($h_t$) effects.

---

## 📖 Citation

If you use this model, concepts, or simulation code in your research, please cite:

```bibtex
@article{sawada2026binary,
  author      = {Sawada, Norimitsu},
  title       = {The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure},
  journal     = {Zenodo Preprint},
  year        = {2026},
  month       = {aug},
  version     = {2.0.0},
  doi         = {10.5281/zenodo.21759689},
  url         = {https://doi.org/10.5281/zenodo.21759689}
}
```

---

## License

This project is licensed under the Creative Commons Attribution 4.0 International License - see the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) details.
