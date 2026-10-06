import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 rolls of a fair six-sided die
np.random.seed(42)
rolls = np.random.randint(1, 7, size=1000)

# Print the first 10 rolls
print("First 10 rolls:", rolls[:10])

# Count occurrences of each face
faces, counts = np.unique(rolls, return_counts=True)

# Calculate and print probabilities
print("\nFace Count Empirical P Theoretical P")

for face, count in zip(faces, counts):
    empirical_probability = count / 1000
    theoretical_probability = 1 / 6

    print(
        f"{face} {count:5d} "
        f"{empirical_probability:.3f} "
        f"{theoretical_probability:.4f}"
    )

# Plot histogram
plt.hist(
    rolls,
    bins=np.arange(0.5, 7.5, 1),
    edgecolor="black"
)

plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("Simulation of 1000 Fair Die Rolls")
plt.xticks(range(1, 7))

# Save the histogram
plt.savefig("die_rolls.png")

print("\nSaved die_rolls.png")

plt.show()