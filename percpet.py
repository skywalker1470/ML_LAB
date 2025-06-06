import numpy as np

# OR dataset inputs and labels
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([0, 1, 1, 1])  # OR output

# Perceptron parameters
weights = np.zeros(X.shape[1])
bias = 0.02
learning_rate = 0.1
epochs = 10

# Activation function (step)
def activation(x):
    return 1 if x >= 0 else 0

# Training loop
for epoch in range(epochs):
    for i in range(len(X)):
        linear_output = np.dot(X[i], weights) + bias
        y_pred = activation(linear_output)
        error = y[i] - y_pred
        weights += learning_rate * error * X[i]
        bias += learning_rate * error

print("Trained weights:", weights)
print("Trained bias:", bias)

# Testing
print("Predictions:")
for i in range(len(X)):
    linear_output = np.dot(X[i], weights) + bias
    print(f"Input: {X[i]} -> Prediction: {activation(linear_output)}")
