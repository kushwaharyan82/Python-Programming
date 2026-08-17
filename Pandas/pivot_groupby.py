import pandas as pd

data = {
    "Name": ["Aryan", "Rahul", "Aman", "Rohit", "Neha", "Priya"],
    "Course": ["AI/ML", "CSE", "AI/ML", "CSE", "AI/ML", "CSE"],
    "Gender": ["M", "M", "M", "M", "F", "F"],
    "Marks": [85, 90, 78, 92, 88, 95]
}

df = pd.DataFrame(data)

# GroupBy with multiple operations
summary = df.groupby("Course")["Marks"].agg(["mean", "max", "min", "count"])

print("Course-wise Summary:")
print(summary)

# Pivot table
pivot = pd.pivot_table(
    df,
    values="Marks",
    index="Course",
    columns="Gender",
    aggfunc="mean"
)

print("\nPivot Table:")
print(pivot)
