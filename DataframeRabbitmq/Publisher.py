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
message1 = ("min(\"Payment\")," + RESPONSE_QUEUE_NAME)
message2 = ("max(\"Payment\")," + RESPONSE_QUEUE_NAME)

#Publishing a message
channel.basic_publish(exchange='logs', routing_key='', body=message1)
channel.basic_publish(exchange='logs', routing_key='', body=message2)



#Creating answer buffer
channel.queue_declare(queue=RESPONSE_QUEUE_NAME, durable=True)


def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(pickle.loads(body))


channel.basic_consume(queue=RESPONSE_QUEUE_NAME, on_message_callback=callback)
channel.start_consuming()

print("The max value is: " + max)