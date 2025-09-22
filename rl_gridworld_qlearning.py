import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# Simple 5x5 gridworld
# S at (0,0), G at (4,4), reward +1 at goal, -0.01 per step
# Actions: 0=up,1=right,2=down,3=left
N = 5
S = (0,0)
G = (4,4)

def step(state, action):
    r, c = state
    if action == 0: r = max(0, r-1)
    elif action == 1: c = min(N-1, c+1)
    elif action == 2: r = min(N-1, r+1)
    elif action == 3: c = max(0, c-1)
    ns = (r,c)
    if ns == G:
        return ns, 1.0, True
    return ns, -0.01, False

def eps_greedy(Q, s, eps):
    if np.random.rand() < eps:
        return np.random.randint(4)
    r, c = s
    return np.argmax(Q[r,c,:])

episodes = 800
alpha = 0.5
gamma = 0.98
eps_start, eps_end = 0.9, 0.05

Q = np.zeros((N,N,4))
rewards = []

for ep in range(episodes):
    eps = eps_end + (eps_start - eps_end)*np.exp(-ep/200)
    s = S
    done = False
    ep_rew = 0.0
    steps = 0
    while not done and steps < 200:
        a = eps_greedy(Q, s, eps)
        ns, r, done = step(s, a)
        r0,c0 = s
        r1,c1 = ns
        best_next = np.max(Q[r1,c1,:])
        td_target = r + gamma*best_next*(0 if done else 1)
        Q[r0,c0,a] += alpha*(td_target - Q[r0,c0,a])
        s = ns
        ep_rew += r
        steps += 1
    rewards.append(ep_rew)

# running average reward
window = 20
ra = np.convolve(rewards, np.ones(window)/window, mode='valid')

plt.figure()
plt.plot(rewards, linewidth=1, label='Episode reward')
plt.plot(np.arange(window-1, episodes), ra, linewidth=2, label='Running avg')
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Q-learning in 5x5 Gridworld (no external frameworks)')
plt.legend()
plt.tight_layout()
plt.savefig('gridworld_qlearning_rewards.png', dpi=150)
print('Saved figure: gridworld_qlearning_rewards.png')
