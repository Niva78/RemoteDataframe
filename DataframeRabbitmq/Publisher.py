from unittest import result
import pika
import sys
import pickle

RESPONSE_QUEUE_NAME = "Min"

#Creating connection to pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

#Stablishing a channel
channel = connection.channel()

#Declaring the exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

#Creating message
message = ("min(\"Payment\")," + RESPONSE_QUEUE_NAME)

#Publishing a message
channel.basic_publish(exchange='logs', routing_key='', body=message)



#Creating answer buffer
channel.queue_declare(queue=RESPONSE_QUEUE_NAME, durable=True)

min = 0
max = 0

def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    global max
    result = pickle.loads(body)
    max = max(max, int(result))


channel.basic_consume(queue=RESPONSE_QUEUE_NAME, on_message_callback=callback)
channel.start_consuming()

print("The max value is: " + max)