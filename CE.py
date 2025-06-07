import pandas as pd

# Load dataset
df = pd.read_csv("enjoysport.csv")

# Preprocess
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Initialize S as the first positive example
for i in range(len(y)):
    if y[i].lower() == 'yes':
        S = list(X.iloc[i])
        break

# Initialize G as the most general hypothesis
G = [["?"] * len(S)]

# Iterate through all examples
for i in range(len(y)):
    instance = list(X.iloc[i])
    label = y[i].lower()

    if label == "yes":
        # Update S: generalize only where needed
        for j in range(len(S)):
            if S[j] != instance[j]:
                S[j] = "?"
        # Remove from G any hypothesis inconsistent with the new S
        G = [g for g in G if all(g[k] == "?" or g[k] == S[k] for k in range(len(g)))]

    elif label == "no":
        # Specialize G
        new_G = []
        for g in G:
            for j in range(len(g)):
                if g[j] == "?":
                    if S[j] != instance[j]:
                        new_hypothesis = g.copy()
                        new_hypothesis[j] = S[j]
                        if all(new_hypothesis[k] == "?" or new_hypothesis[k] == S[k] for k in range(len(new_hypothesis))):
                            new_G.append(new_hypothesis)
        G = new_G

print("Final Specific Hypothesis (S):", S)
print("Final General Hypotheses (G):", G)
