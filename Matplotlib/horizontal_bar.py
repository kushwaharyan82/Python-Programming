import matplotlib.pyplot as plt

subjects = ["Python", "DSA", "SQL", "ML", "AI"]
marks = [85, 78, 90, 88, 92]

plt.barh(subjects, marks)

plt.title("Subject Marks")
plt.xlabel("Marks")
plt.ylabel("Subjects")

plt.show()
