import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# In-code dataset (like play_tennis.csv)

# Create DataFrame
df = pd.read_csv("PlayTennis.csv")

# Split features and target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Convert categorical variables to numeric
X = pd.get_dummies(X)

# Train the decision tree (ID3: uses entropy)
model = DecisionTreeClassifier(criterion='gini')
model.fit(X, y)

# Plot (minimal version: no styling)
tree.plot_tree(model , feature_names=X.columns , class_names = model.classes_ )
plt.show()
