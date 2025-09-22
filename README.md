# Hi! Paris Summer School 2025 — Minimal Reproductions

This mini-repo contains **small, self-contained** Python scripts I reproduced after the summer school to demonstrate hands-on understanding of:
- **Multi-Armed Bandits** (ε-greedy, UCB1, Thompson Sampling)
- **Langevin Dynamics** for sampling in a simple 1D double-well potential
- **Q-learning in a tiny Gridworld** (no external RL frameworks)

> All scripts use only standard Python + `numpy` + `matplotlib`.

## Contents
- `bandits_epsilon_ucb_thompson.py` — simulate K-armed Bernoulli bandit, compare algorithms, and plot cumulative regret.
- `langevin_sampling_double_well.py` — overdamped Langevin sampler; compare histogram to the target density.
- `rl_gridworld_qlearning.py` — Q-learning on a 5x5 grid; plots running average reward.

## How to run
```bash
pip install numpy matplotlib
python bandits_epsilon_ucb_thompson.py
python langevin_sampling_double_well.py
python rl_gridworld_qlearning.py
```

Each script will save its figure(s) as `.png` in the same folder.

## Notes
- These are intentionally **short and didactic**; they’re not optimized.
- Random seeds are fixed for reproducibility.
