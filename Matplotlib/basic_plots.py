import matplotlib.pyplot as plt

# Sample data
subjects = ["Python", "DSA", "SQL", "ML", "AI"]
marks = [85, 78, 90, 88, 92]

# Bar chart
plt.bar(subjects, marks)
plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Line chart
plt.plot(subjects, marks, marker="o")
plt.title("Marks Progress")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
