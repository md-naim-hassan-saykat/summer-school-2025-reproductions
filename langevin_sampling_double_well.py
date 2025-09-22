import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Potential: double well U(x) = x^4/4 - x^2/2
def U(x):
    return x**4/4 - x**2/2

def dUdx(x):
    return x**3 - x

# Target density proportional to exp(-U(x))
def logp(x):  # unnormalized
    return -U(x)

# Overdamped Langevin discretization (ULA)
def langevin_sample(x0=0.0, steps=20000, step=0.01):
    x = x0
    traj = []
    for t in range(steps):
        grad = dUdx(x)
        x = x - step*grad + np.sqrt(2*step)*np.random.randn()
        traj.append(x)
    return np.array(traj)

traj = langevin_sample()
burn = 2000
samples = traj[burn:]

# Plot histogram vs. exp(-U(x)) up to a constant
xs = np.linspace(-3, 3, 400)
unnorm = np.exp(-U(xs))
# normalize for plotting
pdf = unnorm / np.trapz(unnorm, xs)

plt.figure()
plt.hist(samples, bins=60, density=True, alpha=0.6, label='Langevin samples')
plt.plot(xs, pdf, linewidth=2, label=r'Target $\propto e^{-U(x)}$')
plt.xlabel('x')
plt.ylabel('density')
plt.title('Overdamped Langevin in a 1D Double-Well Potential')
plt.legend()
plt.tight_layout()
plt.savefig('langevin_double_well.png', dpi=150)
print('Saved figure: langevin_double_well.png')
