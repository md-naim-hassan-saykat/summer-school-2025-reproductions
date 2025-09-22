import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# ----- Problem setup -----
K = 5  # number of arms
T = 2000  # horizon
true_means = np.random.rand(K)  # Bernoulli means in [0,1]
best_mean = np.max(true_means)
best_arm = np.argmax(true_means)

# ----- Helper: simulate pulls -----
def bernoulli(p, size=1):
    return (np.random.rand(size) < p).astype(float)

# ----- ε-greedy -----
def run_epsilon_greedy(eps=0.1):
    counts = np.zeros(K)
    rewards = np.zeros(K)
    cum_regret = np.zeros(T)
    total_regret = 0.0
    for t in range(T):
        if np.random.rand() < eps:
            a = np.random.randint(K)
        else:
            avg = np.divide(rewards, np.maximum(counts, 1), where=(np.maximum(counts,1)!=0))
            a = np.argmax(avg)
        r = bernoulli(true_means[a])[0]
        counts[a] += 1
        rewards[a] += r
        total_regret += (best_mean - true_means[a])
        cum_regret[t] = total_regret
    return cum_regret

# ----- UCB1 -----
def run_ucb1():
    counts = np.zeros(K)
    rewards = np.zeros(K)
    avg = np.zeros(K)
    cum_regret = np.zeros(T)
    total_regret = 0.0

    # initialize: pull each arm once
    for a in range(K):
        r = bernoulli(true_means[a])[0]
        counts[a] += 1
        rewards[a] += r
        avg[a] = rewards[a] / counts[a]
        total_regret += (best_mean - true_means[a])
        cum_regret[int(a)] = total_regret

    for t in range(K, T):
        ucb = avg + np.sqrt(2*np.log(t+1) / counts)
        a = np.argmax(ucb)
        r = bernoulli(true_means[a])[0]
        counts[a] += 1
        rewards[a] += r
        avg[a] = rewards[a] / counts[a]
        total_regret += (best_mean - true_means[a])
        cum_regret[t] = total_regret
    return cum_regret

# ----- Thompson Sampling (Beta-Bernoulli) -----
def run_thompson():
    alpha = np.ones(K)  # prior Beta(1,1)
    beta = np.ones(K)
    cum_regret = np.zeros(T)
    total_regret = 0.0
    for t in range(T):
        samples = np.random.beta(alpha, beta)
        a = np.argmax(samples)
        r = bernoulli(true_means[a])[0]
        alpha[a] += r
        beta[a] += (1 - r)
        total_regret += (best_mean - true_means[a])
        cum_regret[t] = total_regret
    return cum_regret

eg = run_epsilon_greedy(0.1)
ucb = run_ucb1()
ts = run_thompson()

plt.figure()
plt.plot(eg, label=r'$\epsilon$-greedy (0.1)')
plt.plot(ucb, label='UCB1')
plt.plot(ts, label='Thompson Sampling')
plt.xlabel('Time step')
plt.ylabel('Cumulative regret')
plt.title('K-armed Bernoulli Bandit (K=%d)' % K)
plt.legend()
plt.tight_layout()
plt.savefig('bandit_cumulative_regret.png', dpi=150)
print('Saved figure: bandit_cumulative_regret.png')
