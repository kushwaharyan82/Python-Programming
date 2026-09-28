import matplotlib.pyplot as plt

subjects = ["Python", "DSA", "SQL", "ML", "AI"]
marks = [85, 78, 90, 88, 92]
errors = [3, 5, 2, 4, 3]

plt.errorbar(
    subjects,
    marks,
    yerr=errors,
    marker="o",
    capsize=5
)

plt.title("Marks with Error Range")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
