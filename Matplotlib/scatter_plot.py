import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7]
marks = [45, 50, 58, 65, 72, 80, 88]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
