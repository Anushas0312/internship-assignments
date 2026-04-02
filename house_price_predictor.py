import numpy as np
from sklearn.linear_model import LinearRegression

# Example dataset (House size in square feet vs Price)
house_size = np.array([500, 800, 1000, 1200, 1500, 1800]).reshape(-1,1)
house_price = np.array([150000, 200000, 250000, 300000, 350000, 400000])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(house_size, house_price)

# Test prediction with new input
new_size = np.array([[1400]])
predicted_price = model.predict(new_size)

print("House Size (sq ft):", new_size[0][0])
print("Predicted House Price:", predicted_price[0])