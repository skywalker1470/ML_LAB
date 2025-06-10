import numpy as np 
import pandas as pd 

df = pd.read_csv("enjoysport.csv")

x = df.iloc[: , :-1].values
y = df.iloc[: , -1].values
S = ['-'] * x.shape[1]
G = [['?'] * len(S)]

for i in range(len(y)):
    if (y[i].lower()=='yes'):
        for j in range(len(S)):
            if(S[j]=='-'):
                S[j] = x[i][j]
            elif(S[j]!=x[i][j]):
                S[j] = "?"
        G = [g for g in G if all(g[j]=='?' or g[j]==x[i][j] for j in range(len(S)))]
    
    else:
        new_G = []
        for g in G:
            for j in range(len(S)):
                if(g[j]=='?'):
                    if(S[j]!=x[i][j]):
                        h = g.copy() 
                        h[j] = S[j]
                        new_G.append(h)
                    
        G = new_G
print(S)
print(G)