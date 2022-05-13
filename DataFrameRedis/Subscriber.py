from ast import Subscript
from re import sub
import redis
import pandas as pd
import pickle

#Creating empty dataframe
df = pd.read_csv("test1.csv")

#Server functions
def readcsv(name):
    global df
    df = pd.read_csv(name)
    return df.values.tolist()


def apply(column, cond):
    return df[column].apply(cond)


def columns():
    return df.columns.values.tolist()


def groupby(cond):
    return df.groupby([cond]).mean()


def head(num):
    return df.head(num)


def isin(item):
    return df.isin([item])


def items():
    tuples=[]
    for label, content in df.items():
        tuples.append(content.values.tolist())
    return tuples

def max(column):
    return df[column].max()


def min(column):
    return df[column].min()

#Connecting to Redis
subscriber =  redis.Redis(host="localhost", port=6379, decode_responses=True)

#Creating bridge to pub sub
subscriber_p = subscriber.pubsub()

#Subscribing subscriber into a channel
subscriber_p.subscribe("Functions")

messag = subscriber_p.get_message(ignore_subscribe_messages=True)
while True:
    if messag and messag.get('type') == "message":
        funct, channel = str(messag.get('data')).split('-')
        subscriber.publish(channel, pickle.dumps(eval(funct)))
    messag = subscriber_p.get_message(ignore_subscribe_messages=True)