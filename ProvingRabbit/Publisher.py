import pika
import sys

#Creating connection to pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

#Stablishing a channel
channel = connection.channel()

#Declaring the exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

#Creating message
message = "Hello brother."

#Publishing a message
channel.basic_publish(exchange='logs', routing_key='', body=message)



#GETTING ANSWER
channel.queue_declare(queue='response', durable=True)
print(' [*] Waiting for response("Not nesessary"). To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(" [x] exiting...")
    quit()


channel.basic_consume(queue='response', on_message_callback=callback)
channel.start_consuming()

#Closing connection
connection.close()