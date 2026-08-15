# Binary Anchor Model (BAM) V2.0

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
- **Option A: Clean / Standalone Simulation (Recommended)**  
  Runs instantly in any headless/server/local environment without pandas/seaborn dependencies:
  ```bash
  python bam_engine.py
  ```
- **Option B: Original Paper Simulation Script**  
  The original baseline script used to generate figures in the preprint:
  ```bash
  python bam_simulator.py
  ```

### Outputs Generated:
Both scripts execute in under 1 second and save publication-quality figures (300 dpi) matching Section 8 of the paper:
- `bam_simulation_vulnerable.png` (Dynamics of Master Equation & Hesitation Energy accumulation)
- `bam_comparison_eta.png` (Comparison between Resilient vs. Vulnerable profiles based on Amygdala plasticity $\eta_{A0}$)

---

## 🧠 Overview

The **Binary Anchor Model (BAM)** formalizes human decision-making and cognitive collapse as a two-layer homeostatic structure:
- **System A (Biological Anchor):** Rooted in survival, interoception, and the amygdala.
- **System B (Social Anchor):** Rooted in language, institutions, and the PFC.

Version 2.0 formalizes the Master Equation $A_t = \text{WTA}(V_t) \in \{0, 1\}$ as the apex organizing principle, systematizes all equations within a Level 0–3 modular argument-space structure, and introduces the probabilistic Soft-WTA extension.

### Master Equation:
$$A_t = \mathrm{WTA}(V_t) \in \{0, 1\}$$
$$V_t = r_t \cdot m_t + (1 - r_t) \cdot m_{\mathrm{sys}, t}$$
$$\mathrm{WTA}(V_t) = \theta(V_t - T_{\mathrm{E}})$$

---

## Key Formalizations

- **Master Equation & Soft-WTA:** $A_t \sim \text{Bernoulli}(\sigma(V_t - T_E))$
- **Hesitation Energy ($H_t$) & Accumulated Load ($I_t$):** Dual-trigger mechanisms for computational breakdown (Burst).
- **Neurobiological Grounding of $\eta_{A0}$:** Amygdala sensitivity and plasticity ($\eta_{\mathrm{A}}(t) = \eta_{A0} \cdot (1 - \phi_t)$).
- **Quantification of $T_{\text{recovery}}$ & [R-3] $h_t$ Threshold Modification:** Recovery paths from Type 1 Burst and past violence reinforcement dynamics.

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
