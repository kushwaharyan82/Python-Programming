import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Aryan", "Rahul", "Aman", "Rohit"],
    "Age": [19, 20, 19, 21],
    "Course": ["AI/ML", "CSE", "AI/ML", "CSE"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nFirst 2 rows:")
print(df.head(2))

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nBasic information:")
print(df.info())
