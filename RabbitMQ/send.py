import pickle

import pika
import pandas as pd

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='max')
channel.queue_declare(queue='min')

df = pd.read_csv("fitxer.csv.txt")
print(df)
channel.basic_publish(exchange='', routing_key='max', body= pickle.dumps(df.max()))
channel.basic_publish(exchange='', routing_key='max', body= pickle.dumps(df.min()))

print(" [x] Sent max() and min()")
connection.close()