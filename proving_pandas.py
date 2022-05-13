from cgitb import reset
from unittest import result
import pandas as pd
import pickle


def apply(column, funct):
    print(funct)
    return df1[column].apply(funct)


df1 = pd.read_csv("test1.csv")
columnName = None

newDT = df1.loc[:,"Payment"]


coded = pickle.dumps(df1.groupby(["Name"]).mean())
print(type(coded))

decoded = pickle.loads(coded)
print(decoded)



result = eval("apply(\'Name\', lambda x:x*2)")

print(result)
print(df1['Name'].apply(lambda x:x*2))