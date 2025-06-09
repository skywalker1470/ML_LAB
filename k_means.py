import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 

data = np.array([
    [0.5,0.5],[0,1],[2,3],[3,3],[3.5,3],[4,4],[3,3.5],
    [5,6],[7,9],[8,8],[4,4]
])

model = KMeans(n_clusters=3)
model.fit(data)

centroids = model.cluster_centers_
labels = model.labels_

colors = ['r','g','b' ]
for i in range(len(data)):
    plt.scatter(data[i][0] , data[i][1] , color = colors[labels[i]])
    
#printing centroids 

plt.scatter(centroids[: , 0] , centroids[: ,1] , color = 'y')
plt.show()