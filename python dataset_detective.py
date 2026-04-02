import pandas as pd

# Load dataset (example: CSV file)
# Make sure you place a CSV file in the same folder
df = pd.read_csv("sample_dataset.csv")

print("----- Top 5 Rows -----")
print(df.head())

print("\n----- Highest Value Column (Numerical) -----")
highest_column = df.max(numeric_only=True)
print(highest_column)

print("\n----- Missing Values in Each Column -----")
missing_values = df.isnull().sum()
print(missing_values)