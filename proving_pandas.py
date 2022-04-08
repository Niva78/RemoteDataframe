import pandas as pd
import pickle


df1 = pd.read_csv("test1.csv")
columnName = None

newDT = df1.loc[:,"Payment"]


coded = pickle.dumps(df1.groupby(["Name"]).mean())
print(type(coded))

decoded = pickle.loads(coded)
print(decoded)