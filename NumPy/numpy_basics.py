import numpy as np

# Create an array
numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("Shape:", numbers.shape)
print("Size:", numbers.size)
print("Data type:", numbers.dtype)

# Basic operations
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# Mathematical operation
print("Array × 2:", numbers * 2)
