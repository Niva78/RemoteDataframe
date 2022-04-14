from multiprocessing import connection
import queue
import pika

#Establishing connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

#Creating a communication channel
channel = connection.channel()

#ANSWERING
#Creating a response channel
channel.queue_declare(queue='response', durable=True)


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
    channel.basic_publish(exchange='', routing_key='response', body='What\'s up?')

#Definnig behaviour ones it starts consuming
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

#Infinite listening
channel.start_consuming()