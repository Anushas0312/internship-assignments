import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample Mall Dataset (Income & Spending Score)
data = {
    "CustomerID": [1,2,3,4,5,6,7,8,9,10],
    "Income": [15,16,17,18,19,60,62,64,65,67],
    "SpendingScore": [39,81,6,77,40,50,52,54,56,58]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Selecting features
X = df[["Income", "SpendingScore"]]

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

print("\nClustered Data:")
print(df)

# Plot clusters
plt.figure()
plt.scatter(df["Income"], df["SpendingScore"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()