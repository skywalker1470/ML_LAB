import numpy as np 
from sklearn.neural_network import MLPClassifier

x = np.array([
    [0,0],
    [1,0],
    [0,1],
    [1,1]
])
y = np.array([0,1,1,0])

model = MLPClassifier(hidden_layer_sizes=(2 ,2) , activation="relu" , max_iter= 100000)
model.fit(x,y)

input = [[1,1]]
print(f"The prediction for {input} is {model.predict(input)}")
print(f"The weights are {model.coefs_}")

print(f"The biases are {model.intercepts_}")