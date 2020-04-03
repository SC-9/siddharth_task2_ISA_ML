import pandas as pd
dataset=pd.read_csv('2.12_Health_systems.csv')
print("Number of missing data: ",end="")
print(dataset.isnull().sum().sum())
