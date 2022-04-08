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


def apply(cond):
    return pickle.dumps(df.apply(eval(cond)))


def columns():
    return df.columns.values.tolist()


def groupby(cond):
    return pickle.dumps(df.groupby([cond]).mean())


def head(num):
    return pickle.dumps(df.head(num))


def isin(item):
    return pickle.dumps(df.isin([item]))


def items():
    tuples=[]
    for label, content in df.items():
        tuples.append(content.values.tolist())
    return tuples

def max(column):
    return str(df[column].max())


def min(column):
    return str(df[column].min())

#Connecting to REDIS
subscriber = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
subscription = subscriber.pubsub()
subscription.subscribe('channel')


#Getting connection message
subscription.get_message()

#Infinite listening loop.
operation = None
while True:
    if operation and operation.get('type') == "message":
        function,channel = str(operation['data']).split(',')
        result = eval(function)
        print(result)
        subscriber.publish(str(channel), result)
    operation = subscription.get_message()
