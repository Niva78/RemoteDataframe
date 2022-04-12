import pandas as pd
import pickle
dt = pd.read_csv("test1.csv")

def max(column):
    return str(dt[column].max())


def min(column):
    return str(dt[column].min())