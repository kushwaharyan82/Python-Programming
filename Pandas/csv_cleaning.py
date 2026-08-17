import pandas as pd

# Create sample data
data = {
    "Name": ["Aryan", "Rahul", "Aman", "Rohit", "Neha"],
    "Age": [19, 20, None, 21, 20],
    "Marks": [85, 90, 78, None, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numeric values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Data:")
print(df)

# Basic statistics
print("\nStatistics:")
print(df.describe())
