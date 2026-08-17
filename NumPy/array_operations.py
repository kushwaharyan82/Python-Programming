import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

# Arithmetic operations
print("Original:", numbers)
print("Add 5:", numbers + 5)
print("Multiply by 2:", numbers * 2)
print("Square:", numbers ** 2)

# Comparison
print("\nGreater than 25:")
print(numbers > 25)

# Filtering
filtered = numbers[numbers > 25]

print("\nFiltered values:", filtered)

# Sum and average
print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))
