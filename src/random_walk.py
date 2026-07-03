import matplotlib.pyplot as plt
import numpy as np

def generate_1D_random_walk(steps, choices, probs):
    walk = np.random.choice(choices, size=steps, p=probs)

    positions = np.insert(np.cumsum(walk), 0, 0)  # Start at position 0

    return walk, positions, np.cumsum(walk)

def plot_1D_random_walk(steps, positions):
    plt.figure(figsize=(10, 5))
    plt.plot(positions, label="Random Walk Path", color="blue", linewidth=1)

    plt.scatter(0, positions[0], color="green", s=100, label="Start (0)", zorder=5)
    plt.scatter(steps, positions[-1], color="red", s=100, label=f"End ({positions[-1]})", zorder=5)

    plt.title("1D Random Walk Simulation", fontsize=14)
    plt.xlabel("Number of Steps (Time)", fontsize=12)
    plt.ylabel("Position", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()