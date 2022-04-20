import redis
import pandas as pd
import pickle

#Connecting to redis server as a publisher
publisher = redis.Redis(host='localhost', port=6379)

#Publish the function that user wants from the workers
publisher.publish('Functions', 'head(6)-Head')

#Create a publisher
publisher_p = publisher.pubsub()

#Subscribing to a channel
publisher_p.subscribe('Head')

#Waiting loop for answer
answered = False
messag = publisher_p.get_message(ignore_subscribe_messages=True)
while not answered:
    if messag and messag.get('type'):
        print(pickle.loads(messag.get('data')))
        answered = True
    messag = publisher_p.get_message(ignore_subscribe_messages=True)
