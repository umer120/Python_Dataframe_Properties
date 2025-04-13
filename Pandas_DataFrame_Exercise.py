import pandas as pd
import numpy as np

data = [
    [101,'Alice',25,50000,'HR'],
    [102,'Bob',30,60000,'IT'],
    [103,'Charlie',28,55000,'Finance'],
    [104,'David',35,70000,'IT'],
    [105,'Ema',27,65000,'HR']      
]

df = pd.DataFrame(data, columns=["ID","Name","Age","Salary","Department"])


# Extract only the Name and Salary columns.
print("Task1: Extracting Name and Salary columns only")
print(df[["Name","Salary"]])

# Extract rows where Age > 28
print("\n\nTask2: Extracting rows based on some condition i.e. Age > 28")
print(df[df['Age'] > 28])

# Increase the Salary of employees in HR by 5%.
df.loc[df['Department'] == 'HR', "Salary"] +=  df.loc[df['Department'] == 'HR', "Salary"]*0.05
print("\n\nTask3:\nAfter increasing the salaries:")
print(df)

# Introduce a few NaN values in Salary and Department
df.loc[2,"Salary"] = np.nan
df.loc[3,"Salary"] =np.nan
df.loc[4,"Department"]=np.nan
print("\n\nTask4:\nAfter introducing nan values:")
print(df)

# Add new column with 10% increase in salary
increased = df["Salary"]*0.1
df["salary_increased"] = df["Salary"]+increased
print("\n\nTask5:\nAfter adding another column by increasing salary:")
print(df)


# Drop Age Column
df.drop(columns=["Age"],inplace=True)
print("\n\nTask6:\nAfter dropping age:")
print(df)
