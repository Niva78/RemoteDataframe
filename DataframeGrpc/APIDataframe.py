import pandas as pd
import pickle
dt = pd.read_csv("test1.csv")

def min():
    return dt.min().to_string()

def max():
    return dt.max().to_string()