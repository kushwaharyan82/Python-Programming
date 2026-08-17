import pandas as pd

students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Name": ["Aryan", "Rahul", "Aman", "Rohit"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Marks": [85, 90, 78, 92]
})

# Merge
merged = pd.merge(students, marks, on="Student_ID")

print("Merged Data:")
print(merged)

# Concat
extra_students = pd.DataFrame({
    "Student_ID": [5, 6],
    "Name": ["Neha", "Priya"]
})

combined = pd.concat([students, extra_students], ignore_index=True)

print("\nConcatenated Data:")
print(combined)
