import pandas as pd

data = {
    "Name": ["Aryan", "Rahul", "Aman", "Rohit", "Neha"],
    "Age": [19, 20, 19, 21, 20],
    "Course": ["AI/ML", "CSE", "AI/ML", "CSE", "AI/ML"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

# Filtering
print("Students with marks above 85:")
print(df[df["Marks"] > 85])

# Sorting
print("\nSorted by marks:")
print(df.sort_values("Marks", ascending=False))

# GroupBy
print("\nAverage marks by course:")
print(df.groupby("Course")["Marks"].mean())

# Maximum marks
print("\nHighest marks:")
print(df["Marks"].max())
