import pandas as pd
import numpy as np

data = [
    [1,'Alice',30,'Engineer'],
    [2,'Bob',np.nan,'Doctor'],
    [3,'Charlie',35,'Teacher'],
    [4,'David',40,np.nan],
    [5,'Eve',28,'Artist'],
    [2,'Bob',np.nan,'Doctor'],
    [4,'David',40,np.nan]        
]

df = pd.DataFrame(data, columns=["ID","Name","Age","Profession"])

print(df)


# Fill missing values
#df = df.fillna(value="Unknown")

print(df)


print("\n\n",df.info(),"\n\n")

print(df.describe())

print(df.shape)

print(df.columns)


# Filter rows based on conditions
print(df[df['Age'] > 28])

print("\n",df[df['Name'] == 'Alice'])

print("\n",df[(df['Age'] > 25) & (df['ID'] > 4)])


# Sort and Multi-Column Sort
df_sorted = df.sort_values(by='Age', ascending=True)
print("\n",df_sorted,"\n")


df_sorted = df.sort_values(by=['Age', 'ID'], ascending=[True,False])
print(df_sorted)

# Create a column
df["Salary"] = np.nan
print(df)

# Drop a column
df.drop(columns=['Salary'], inplace=True)

print(df)

# Exporting data frame to CSV or Excel
df.to_csv('data.csv', index=False)
df.to_excel('data.xlsx',index=False)

# Change a single value in the dataframe
df.at[2, 'Age'] = 29

df.iloc[2,2]=29

print(df)
