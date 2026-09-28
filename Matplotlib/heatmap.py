import matplotlib.pyplot as plt
import numpy as np

marks = np.array([
    [85, 78, 90],
    [72, 88, 95],
    [80, 75, 85]
])

plt.imshow(marks)

plt.colorbar()

plt.title("Marks Heatmap")
plt.xlabel("Subjects")
plt.ylabel("Students")

plt.show()
