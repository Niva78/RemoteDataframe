import pickle

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.queue_declare(queue='sender')
channel.queue_declare(queue='response')

channel.basic_publish(exchange='logs', routing_key='', body="df.max()")
channel.basic_publish(exchange='logs', routing_key='', body="df.min()")
print(channel.basic_get(queue='response')[2])
pickle.loads(channel.basic_get(queue='response')[2])

print(" [x] Sent max")
print(" [x] Sent min")

connection.close()