import pandas as pd

# Load the dataset
data = pd.read_csv("enjoysport.csv")

# Get the attribute columns (all except the last)
attrs = data.columns[:-1]

# Initialize S and G
S = list(data.iloc[0][:-1])  # Start with the first positive example
G = [["?"] * len(S)]         # G starts with the most general hypothesis

# Process each training example
for i in range(len(data)):
    row = data.iloc[i]
    x, y = list(row[:-1]), row[-1]

    if y == "yes":
        # Update S to be more general if needed
        for j in range(len(S)):
            if S[j] != x[j]:
                S[j] = "?"
        # Remove G hypotheses that don't match this positive example
        G = [g for g in G if all(g[k] == "?" or g[k] == x[k] for k in range(len(g)))]

    else:  # y == "no"
        G_new = []
        for g in G:
            for j in range(len(g)):
                if g[j] == "?":
                    for val in data[attrs[j]].unique():
                        if val != x[j]:
                            new_hypo = g.copy()
                            new_hypo[j] = val
                            if all(S[k] == "?" or S[k] == new_hypo[k] for k in range(len(S))):
                                G_new.append(new_hypo)
        G = G_new

# Print final S and G
print("Final Specific Hypothesis (S):", S)
print("Final General Hypotheses (G):")
for g in G:
    print(g)
