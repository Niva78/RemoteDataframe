import pickle

import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='max')
    channel.queue_declare(queue='min')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % pickle.loads(body))

    channel.basic_consume(queue='max', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='min', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)