import pandas as pd

# Load the dataset
df = pd.read_csv("enjoysport.csv")

# Initialize the hypothesis with '-'
hypothesis = ["-"] * (len(df.columns)-1)  # exclude the 'enjoy' column

# Iterate through each row where enjoy == 'yes'
for index, row in df.iterrows():
    if row["enjoy"].lower() == "yes":
        for i in range(len(hypothesis)):
            attr_value = row[i]
            if hypothesis[i] == "-":
                hypothesis[i] = attr_value
            elif hypothesis[i] != attr_value:
                hypothesis[i] = "?"
    else: #negative hypo
        flag = True
        for i in range(len(hypothesis)):
            if(hypothesis[i]!=row[i] and row[i] != '?'):
                flag = False
                break
        if(flag):
            for i in range(len(hypothesis)):
                if(hypothesis[i]==row[i]):
                    hypothesis[i] = "?"
    
                

# Output the final hypothesis
print(hypothesis)
