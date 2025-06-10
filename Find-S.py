import numpy as np 
import pandas as pd 

df = pd.read_csv("enjoysport.csv")

hypo = ["-"] * (len(df.columns)-1)

for idx , rows in df.iterrows():
    if (rows.iloc[-1].lower() == "yes") : 
        for i in range(len(hypo)):
            if(hypo[i] == '-'):
                hypo[i] = rows[i]
            elif(hypo[i] != rows[i] ):
                hypo[i] = "?"

print(hypo)