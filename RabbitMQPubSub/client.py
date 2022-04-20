import pickle
import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.basic_publish(exchange='logs', routing_key='', body='max(\"A\")')
channel.basic_publish(exchange='logs', routing_key='', body='min(\"A\")')

print(" [x] Sent max")
print(" [x] Sent min")

print(pickle.loads(channel.basic_get(queue='response')[2]))
print(pickle.loads(channel.basic_get(queue='response')[2]))

connection.close()