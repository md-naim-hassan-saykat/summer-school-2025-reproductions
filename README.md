# Summer School 2025 — Minimal Reproductions

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
Dependencies are listed in `requirements.txt`. To install:

```bash
pip install -r requirements.txt
```   

## How to Run
After installing dependencies, run any script:

```bash
python bandits_epsilon_ucb_thompson.py
python langevin_sampling_double_well.py
python rl_gridworld_qlearning.py
```
## License
This project is licensed under the terms of the MIT license (see LICENSE).

## Acknowledgment
These reproductions were created as part of my learning during the Hi! Paris Summer School 2025.
They complement my written report submitted for academic credit.
