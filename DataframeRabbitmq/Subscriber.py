import queue
import pika
import pandas as pd
import pickle

#API dataframe
df = pd.read_csv('test1.csv')

def max(column):
    return df[column].max()


def min(column):
    return df[column].min()

#Establishing connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

#Creating a communication channel
channel = connection.channel()

#Creating an exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

#Declaring a new buffer queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#Creating a bind to a queue
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

#Method to receive messages
def callback(ch, method, properties, body):
    print(" [*] Getting incoming message %r" % body.decode())
    response = body.decode()
    funct, chnnl = str(response).split(',')
    channel.basic_publish(exchange='', routing_key=chnnl, body=pickle.dumps(eval(funct)))

#Definnig behaviour ones it starts consuming
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

#Infinite listening
channel.start_consuming()