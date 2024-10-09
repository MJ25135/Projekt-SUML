import pandas as pd
import sys

from pandas import read_sql

df = pd.read_csv('data/student-mat.csv' , nrows=1)

headers = df.columns.tolist()
print(headers)




# Po czyszczeniu
df = pd.read_csv('data/student-mat.csv' , skiprows=1)

X = df.iloc[:,:-1].values

Y = df.iloc[:,-1].values

print(X)
print(Y)

