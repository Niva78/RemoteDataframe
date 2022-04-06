import pandas as pd



df1 = pd.read_csv("test1.csv")
columnName = None

newDT = df1.loc[:,"Payment"]

print(df1.groupby(['Date']).mean())