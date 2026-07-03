import matplotlib.pyplot as plt
import numpy as np

def generate_1D_random_walk(steps, choices = [], probs = []):
    """
    Generates a single 1D random walk.

    Parameters:
    - steps: Number of steps in the random walk.
    - choices: Possible step for the walk.
    - probs: Probabilities associated with each step size.

    Returns:
    - walk: The sequence of steps taken in the random walk.
    - positions: The cumulative positions after each step.
    """

    walk = np.random.choice(choices, size=steps, p=probs)

    positions = np.insert(np.cumsum(walk), 0, 0)  # Start at position 0

    return walk, positions

def generate_1D_random_walks(num_walks, steps = [], choices = [], probs = []):
    all_walks = []
    all_positions = []

    for _ in range(num_walks):
        walk, positions, cumulative_sum = generate_1D_random_walk(steps, choices, probs)
        all_walks.append(walk)
        all_positions.append(positions)

    return all_walks, all_positions

def plot_1D_random_walks(positions = []):
    plt.figure(figsize=(10, 5))

    for i in range(len(positions)):
        plt.plot(positions[i], label=f"Random Walk {i+1}", linewidth=1)

        #plt.scatter(0, positions[i][0], color="green", s=100, label="Start (0)", zorder=5)
        #plt.scatter(len(positions[i]), positions[i][-1], color="red", s=100, label=f"End ({positions[i][-1]})", zorder=5)

    plt.title("1D Random Walk Simulation", fontsize=14)
    plt.xlabel("Number of Steps (Time)", fontsize=12)
    plt.ylabel("Position", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()

_, positions_1 = generate_1D_random_walk(steps=100, choices=[-1, 1], probs=[0.5, 0.5])
_, positions_2 = generate_1D_random_walk(steps=100, choices=[-1, 1], probs=[0.5, 0.5])
_, positions_3 = generate_1D_random_walk(steps=100, choices=[-1, 1], probs=[0.5, 0.5])

plot_1D_random_walks(positions=[positions_1, positions_2, positions_3])  