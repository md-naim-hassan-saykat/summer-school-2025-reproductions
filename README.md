# Summer School 2025 — Minimal Reproductions

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This repository contains small, self-contained Python scripts I reproduced after attending the **Hi! Paris Summer School 2025**.  
The goal is to consolidate my learning in **bandits, reinforcement learning, and Langevin dynamics** through hands-on coding exercises.

## Contents
- **Multi-Armed Bandits**  
  `bandits_epsilon_ucb_thompson.py`  
  Implements and compares:
  - ε-greedy
  - UCB1
  - Thompson Sampling  
  Plots cumulative regret across time steps.  
  ![Bandit result](bandit_cumulative_regret.png)

- **Langevin Dynamics**  
  `langevin_sampling_double_well.py`  
  Uses overdamped Langevin sampling in a 1D double-well potential.  
  Compares sampled histogram with theoretical density.  
  ![Langevin result](langevin_double_well.png)

- **Reinforcement Learning (Q-learning)**  
  `rl_gridworld_qlearning.py`  
  Q-learning on a 5×5 gridworld with simple rewards.  
  Plots episode reward and running average.  
  ![Q-learning result](gridworld_qlearning_rewards.png)

## Requirements
```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux (zsh/bash)
pip install -r requirements.txt
```   

## How to Run
```bash
python3 bandits_epsilon_ucb_thompson.py
python3 langevin_sampling_double_well.py
python3 rl_gridworld_qlearning.py
```

## License
This project is licensed under the terms of the MIT license (see LICENSE).

## Acknowledgment
These reproductions were created as part of my learning during the Hi! Paris Summer School 2025.
They complement my written report submitted for academic credit.
