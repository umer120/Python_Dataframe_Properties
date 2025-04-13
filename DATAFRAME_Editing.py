import pandas as pd
import numpy as np

data = {
    "Name": ["Ali","Sara","Ahmed","Zara","Bilal","Bilal",""],
    "Age":[25,30,22,28,35,35,np.nan],
    "City":["Lahore","Karachi","Islamabad","Peshawar","Quetta","Quetta",""]        
}

df = pd.DataFrame(data)

# Read the first few rows using head()
print(df.head()) # Default behaviour reads the first 5 rows
print(df.head(3),"\n\n")
print(df.tail()) # Reads the last 5 rows

print("\n\nIf we want to read a specific column:")
print(df["Name"])
print(df[["Name","City"]])

print("\n\n",df[2:4])
print("\n\n",df.iloc[2:4],"\n\n")

print(df.loc[2:3,["Name","City"]],"\n\n")

print(df["Name"].unique())

print(df.sample(4))

print(df.shape) # displays (rows,columns)

print(df.drop_duplicates()) # removes duplicates

print(df.dropna())

