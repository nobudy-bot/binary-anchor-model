# Binary Anchor Model (BAM) V2.0
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21759689.svg)](https://doi.org/10.5281/zenodo.21759689)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the official Python simulation code for the paper:  
**"The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure"** by **Norimitsu Sawada**.

- **Zenodo Preprint (V2.0.0):** [DOI: 10.5281/zenodo.21759689](https://doi.org/10.5281/zenodo.21759689)
- **Concept DOI (All Versions):** [DOI: 10.5281/zenodo.21566423](https://doi.org/10.5281/zenodo.21566423)
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/

---

## Overview

The Binary Anchor Model (BAM) describes decision-making as a two-layer homeostatic structure:
- **System A (Biological Anchor):** Rooted in survival, interoception, and the amygdala.
- **System B (Social Anchor):** Rooted in language, institutions, and the PFC.

Version 2.0 formalizes the Master Equation $A_t = \text{WTA}(V_t) \in \{0, 1\}$ as the apex organizing principle, systematizes all equations within a Level 0–3 modular argument-space structure, and introduces the probabilistic Soft-WTA extension.

---

## Key Formalizations

- **Master Equation & Soft-WTA:** $A_t \sim \text{Bernoulli}(\sigma(V_t - T_E))$
- **Hesitation Energy ($H_t$) & Accumulated Load ($I_t$):** Dual-trigger mechanisms for computational breakdown (Burst).
- **Neurobiological Grounding of $\eta_{A0}$:** Amygdala sensitivity and plasticity ($\eta_A(t) = \eta_{A0} \cdot (1 - \phi_t)$).
- **Quantification of $T_{\text{recovery}}$ & [R-3] $h_t$ Threshold Modification:** Recovery paths from Type 1 Burst and past violence reinforcement dynamics.

---

## Simulation

Run the BAM simulator (requires `numpy`, `matplotlib`, `pandas`, `seaborn`):

<pre><code>python bam_simulator.py</code></pre>

---

## Citation

If you use this model, concepts, or simulation code in your research, please cite:

<pre><code>@techreport{sawada2026binary,
  author      = {Sawada, Norimitsu},
  title       = {The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure},
  institution = {Zenodo},
  year        = {2026},
  month       = {aug},
  version     = {2.0.0},
  doi         = {10.5281/zenodo.21759689},
  url         = {https://doi.org/10.5281/zenodo.21759689}
}</code></pre>

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
