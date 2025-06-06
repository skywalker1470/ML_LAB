import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load data
data = pd.read_csv("data.csv")

# Define features and target
X = data[['Hours']]  # input: 2D
y = data['Score']    # output: 1D

# Split into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Print test predictions vs actual
print("Actual Scores:", list(y_test))
print("Predicted Scores:", list(y_pred))

# Plot
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Line')
plt.xlabel("Hours")
plt.ylabel("Score")
plt.title("Linear Regression (Test Data)")
plt.legend()
plt.show()
