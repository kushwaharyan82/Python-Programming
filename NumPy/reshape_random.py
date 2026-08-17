import numpy as np

# Zeros and ones
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))

print("Zeros:")
print(zeros)

print("\nOnes:")
print(ones)

# Random numbers
random_numbers = np.random.randint(1, 100, 5)

print("\nRandom numbers:")
print(random_numbers)

# Reshape
numbers = np.arange(1, 13)
matrix = numbers.reshape(3, 4)

print("\nOriginal array:")
print(numbers)

print("\nReshaped 3x4 matrix:")
print(matrix)
