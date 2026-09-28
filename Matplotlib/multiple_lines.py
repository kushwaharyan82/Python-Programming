import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

python_marks = [70, 75, 78, 82, 88, 92]
dsa_marks = [60, 65, 68, 72, 76, 80]

plt.plot(months, python_marks, marker="o", label="Python")
plt.plot(months, dsa_marks, marker="o", label="DSA")

plt.title("Python vs DSA Progress")
plt.xlabel("Months")
plt.ylabel("Marks")

plt.legend()

plt.show()
