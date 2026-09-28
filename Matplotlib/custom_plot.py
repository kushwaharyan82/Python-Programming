import matplotlib.pyplot as plt

subjects = ["Python", "DSA", "SQL", "ML", "AI"]
marks = [85, 78, 90, 88, 92]

plt.figure(figsize=(8, 5))

plt.plot(
    subjects,
    marks,
    marker="o",
    linestyle="--",
    linewidth=2,
    label="Marks"
)

plt.title("My Subject Performance")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.grid(True)
plt.legend()

plt.show()
