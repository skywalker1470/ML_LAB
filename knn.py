import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split

data = load_iris()
x = data.data
y = data.target

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size= 0.2)

model = KNeighborsClassifier(n_neighbors= 4)
model.fit(x,y)

y_pred = model.predict(x_test)
print(f"Iris dataset {x_test[1:5]}")
print(f"Predicted Iris predicted classes {y_pred[1:5]}")
print(f"Predicted Iris actual classes {y_test[1:5]}")

acc = accuracy_score(y_test , y_pred)
print(f"The accuracy score is : {acc}")