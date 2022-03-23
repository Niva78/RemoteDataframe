import redis
import pandas as pd
import pickle





#Client subscriber
client_1 = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
client_1.publish('channel-min', 'min(),ResultRead')

client_1p = client_1.pubsub()
client_1p.subscribe('ResultRead')

client_1p.get_message()


answer = False
operation = None
while True:
    if operation != None:
        if operation['data'] != 1:
            print (operation['data'])
            answer = True
    operation = client_1p.get_message()