import matplotlib.pyplot as plt

subjects = ["Python", "DSA", "SQL", "ML", "AI"]
marks = [85, 78, 90, 88, 92]

plt.subplot(1, 2, 1)
plt.bar(subjects, marks)
plt.title("Bar Chart")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.plot(subjects, marks, marker="o")
plt.title("Line Chart")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
