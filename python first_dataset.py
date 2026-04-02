import pandas as pd

data = {
    "Study_Hours": [1,2,3,4,5,6,7,8,9,10],
    "Marks": [40,45,50,55,60,65,70,75,85,92]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nFeatures:", df.columns[0])
print("Label:", df.columns[1])

correlation = df["Study_Hours"].corr(df["Marks"])

print("\nRelationship between study hours and marks:", correlation)