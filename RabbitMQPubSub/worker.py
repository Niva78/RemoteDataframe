import pickle
import pandas as pd
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.queue_declare(queue='sender')
channel.queue_declare(queue='response')

channel.queue_bind(exchange='logs', queue='sender')
channel.queue_bind(exchange='logs', queue='response')

print(' [*] Waiting for logs. To exit press CTRL+C')

df = pd.read_csv("fitxer.csv")


def max(column):
    return df[column].max()


def min(column):
    return df[column].min()


def callback(ch, method, properties, body):
    result = eval(body)
    print(result)
    channel.basic_publish(exchange='', routing_key='response', body=pickle.dumps(result))

channel.basic_consume(queue='sender', on_message_callback=callback, auto_ack=True)


channel.start_consuming()