import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample dataset (Income vs Spending Score)
data = {
    "Income": [15,16,17,18,19,60,62,64,65,67],
    "SpendingScore": [39,81,6,77,40,50,52,54,56,58]
}

df = pd.DataFrame(data)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(df)

print("Customer Segments:")
print(df)

# Visualization
plt.scatter(df["Income"], df["SpendingScore"], c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()