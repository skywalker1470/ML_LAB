import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


data = pd.read_csv("3d.csv")


X = data.iloc[: , [1]] 
y = data.iloc[: , 2]    


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Actual Scores:", list(y_test))
print("Predicted Scores:", list(y_pred))


plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Line')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression (Test Data)")
plt.legend()
plt.show()