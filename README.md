# The Binary Anchor Model: Simulation Code

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21566424.svg)](https://doi.org/10.5281/zenodo.21566424)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the official Python simulation code for the paper:  
**"The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure"** by **Norimitsu Sawada**.

- **Paper DOI (Zenodo)**: [10.5281/zenodo.21566424](https://doi.org/10.5281/zenodo.21566424)
- **Jxiv Preprint**: Pending (JST)

---

## Overview

The script `binary_anchor_simulation.py` reproduces the discrete-time dynamic system simulation (Figure 2) presented in Chapter 3 of the paper. It models the dynamic interactions between:

- **System Alignment ($A_t$)**: Internal/external coherence.
- **Cognitive/Institutional Load ($L_t$)**: Accumulated decision fatigue and rule overhead.
- **Internal Measurement Metric ($m_t$)**: The internal "ruler" used to interpret symbols.
- **Responsibility Allocation Parameter ($r$)**: Subjective agency ($r \to 1$) vs. system dependency ($r \to 0$).

*Note: This model also simulates System B over-reliance ($r \to 0$), corresponding to AI automation bias, agentic delegation, and recursive model collapse.*

---

## Dynamic Scenarios

Executing the script demonstrates three system bifurcations:
1. **Scenario 1: Adaptive Convergence** ($r = 0.5$) — Stable self-correction and load decay.
2. **Scenario 2: Dynamic Oscillation** ($r$ alternates) — Periodic floating of responsibility and persistent stack.
3. **Scenario 3: Critical Burst** ($r \to 0.02$) — Complete delegation to rules/AI, leading to exponential load accumulation ($L_t \ge 15.0$), freeze ($k_t \approx 0$), and non-linear system failure.

---

## How to Run

### Prerequisites
- Python 3.x
- NumPy
- Matplotlib

### Execution
```bash
python binary_anchor_simulation.py
```

### Citation
If you use this model, concepts, or simulation code in your research, please cite:

@article{sawada2026binary,
  title={The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure},
  author={Sawada, Norimitsu},
  year={2026},
  doi={10.5281/zenodo.21566424},
  publisher={Zenodo},
  url={https://doi.org/10.5281/zenodo.21566424}
}
