import redis
import pandas as pd





#Client subscriber
client_1 = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
client_1.publish('channel-min', 'readcsv(\"test1.csv\"),ResultMin')

client_1p = client_1.pubsub()
client_1p.subscribe('ResultMin')

client_1p.get_message()


answer = False
operation = None

while not answer:
    if operation != None:
        print (operation['data'])
        answer = True
    operation = client_1p.get_message()