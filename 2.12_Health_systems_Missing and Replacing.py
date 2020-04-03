import numpy as np
import pandas as pd
dataset=pd.read_csv('2.12_Health_systems.csv')
temp=pd.read_csv('2.12_Health_systems.csv')
print(dataset.isnull().sum().sum())
x=dataset.iloc[:,3:].values
y=dataset.iloc[:,3:].values
#Deletion if column has null in it
a=['improve health system','health system does not matter']
for i in range(0,1):
    n=temp[a[i]]
    t=n.isnull().sum().sum()
    if(t!=0):
        temp.drop(columns=a[i],inplace=True)
#Replacing with mean
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan,strategy= 'mean',verbose=0)
imputer = imputer.fit(x[:,:])
x[:,:] = imputer.transform(x[:,:])
