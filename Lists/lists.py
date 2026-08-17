numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)
print("First element:", numbers[0])

numbers.append(60)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
