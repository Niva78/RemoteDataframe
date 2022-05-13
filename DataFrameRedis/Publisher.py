from asyncio.windows_events import NULL
from email import contentmanager
from socket import timeout
import redis
import pandas as pd
import pickle
import time


#Connecting to redis server as a publisher
publisher = redis.Redis(host='localhost', port=6379)

#Order of the incomming request
requestU = ['Apply', 'Columns', 'GroupBy', 'isin', 'items', 'max', 'min']

#Publish the function that user wants from the workers
publisher.publish('Functions', 'apply(\'Payment\',lambda x:x + 3)-Head')
publisher.publish('Functions', 'columns()-Head')
publisher.publish('Functions', 'groupby(\'Name\')-Head')
publisher.publish('Functions', 'isin(\'Name\')-Head')
publisher.publish('Functions', 'items()-Head')
publisher.publish('Functions', 'max(\'Name\')-Head')
publisher.publish('Functions', 'min(\'Name\')-Head')

#Create a publisher
publisher_p = publisher.pubsub()

#Subscribing to a channel
publisher_p.subscribe('Head')

#As we can know how many worker there will be in the system, we are going to implement a loop that
#ends after a certain amount of time seconds, like a ttl.
timetolive = time.time() + 10


messag = NULL
counterMessages = 0
while True:

    #Response treatement
    if messag and messag.get('type'):
        print("The incomming request is: " + requestU[counterMessages])
        print(pickle.loads(messag.get('data')))
        timetolive = timetolive + 10
        counterMessages += 1
    
    #Time control
    if time.time() > timetolive:
        break
    
    #Getting message
    messag = publisher_p.get_message(ignore_subscribe_messages=True)

    #Stoping cpu from inneseraty iterations
    time.sleep(0.5)
