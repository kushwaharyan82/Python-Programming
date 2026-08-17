import numpy as np

# Create a 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matrix:")
print(matrix)

print("\nShape:", matrix.shape)

# Indexing
print("\nFirst row:", matrix[0])
print("First element:", matrix[0, 0])
print("Last element:", matrix[-1, -1])

# Slicing
print("\nFirst two rows:")
print(matrix[:2])

print("\nFirst two columns:")
print(matrix[:, :2])

# Transpose
print("\nTranspose:")
print(matrix.T)
