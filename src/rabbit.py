import pika

from .settings import settings

message = list()


def add_message(text):
    connection = pika.BlockingConnection(pika.ConnectionParameters(settings.rabbit_host))
    channel = connection.channel()
    channel.queue_declare(queue='test')
    channel.basic_publish(exchange='', routing_key='test', body=text)
    connection.close()


def read_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(settings.rabbit_host))
    channel = connection.channel()
    channel.queue_declare(queue='test')
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        message.append(body)
    channel.basic_consume(queue='test',on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
