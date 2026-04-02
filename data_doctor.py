import pandas as pd

# Load dataset
df = pd.read_csv("sample_dataset.csv")

print("Original Dataset:")
print(df)

# Handle missing values (fill with mean for numerical columns)
df['Math'].fillna(df['Math'].mean(), inplace=True)
df['Science'].fillna(df['Science'].mean(), inplace=True)
df['English'].fillna(df['English'].mean(), inplace=True)

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize text (make names lowercase)
df['Name'] = df['Name'].str.lower()

print("\nCleaned Dataset:")
print(df)