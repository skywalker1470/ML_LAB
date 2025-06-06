import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('your_data.csv')  # Replace 'your_data.csv' with your actual CSV file path

# Assuming your CSV has columns named 'x', 'y', and 'z'
X = df[['x', 'y']]  # Features
y = df['z']         # Target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Plot actual vs predicted values
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # 45-degree line (perfect prediction)
plt.xlabel('Actual z values')
plt.ylabel('Predicted z values')
plt.title('Actual vs Predicted z values')
plt.show()
