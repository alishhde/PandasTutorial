import pandas as pd

df = pd.read_csv('D:\\Teachers\\Dr  M. Babagoli\\Data Mining - Fall 1400\\DataSet\\BruteForce.csv')

print(df.head())
print(df.info())

df2 = df.astype({"'Dst Port'":"int64"})
print(df2.head())
print(df2.info())