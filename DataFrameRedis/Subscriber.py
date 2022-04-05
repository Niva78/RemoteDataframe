import redis
import pandas as pd
import pickle

#Creating empty dataframe
df = pd.DataFrame({'A' : []})

#Server functions
def readcsv(name):
    global df
    df = pd.read_csv(name)
    return df.values.tolist()


def applydf(cond):
    return df.apply(eval(cond)).values.tolist()


def columns():
    return df.columns.values.tolist()


def groupby(cond):
    return pickle.dumps(df.groupby(cond))


def head():
    return df.head(1).values.tolist()


def isin():
    return df.isin([1])


def items():
    tuples=[]
    for label, content in df.items():
        tuples.append(content.values.tolist())
    return tuples

def max():
    return pickle.dumps(df.max())


def min():
    return df.min()

#Connecting to REDIS
subscriber = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
subscription = subscriber.pubsub()
subscription.psubscribe('channel-*')


#Getting connection message
subscription.get_message()

#Infinite listening loop.
operation = None
while True:
    if operation != None:
        if operation['data'] != 1:
            function,channel = str(operation['data']).split(',')
            result = eval(function)
            subscriber.publish(str(channel), str(result))
    operation = subscription.get_message()
