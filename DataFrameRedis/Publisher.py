import redis
import pandas as pd
import pickle





#Client subscriber
client_1 = redis.Redis(host='localhost', port=6379, decode_responses=True)
client_1.publish('channel', 'groupby(\"Name\"),ResultRead')

client_1p = client_1.pubsub()
client_1p.subscribe('ResultRead')


answer = False
messag = None
while not answer:
    if messag != None and messag.get('type') == "message":
        print("The message is:")
        print(messag['data'])
        answer = True
    messag = client_1p.get_message()