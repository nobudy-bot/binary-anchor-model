# The Binary Anchor Model: Simulation Code

This repository contains the Python simulation code for the paper:
**"The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure"** by Norimitsu Sawada.

## Overview
The script `binary_anchor_simulation.py` reproduces the system dynamics simulation (Figure 2) presented in Chapter 3 of the paper. It models the dynamic interactions between:
- System Alignment ($A_t$)
- Cognitive/Institutional Load ($L_t$)
- Internal Measurement Metric ($m_t$)
- Responsibility Allocation Parameter ($r$)

It demonstrates three bifurcation scenarios:
1. **Scenario 1: Adaptive Convergence** ($r = 0.5$)
2. **Scenario 2: Dynamic Oscillation** ($r$ alternates)
3. **Scenario 3: Critical Burst** ($r \to 0.02$)

## Prerequisites
- Python 3.x
- NumPy
- Matplotlib

## How to Run
```bash
python binary_anchor_simulation.py
