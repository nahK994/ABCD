import pika
import json

def publish(event):
    params = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='admin')
    event = json.dumps(event)
    channel.basic_publish(exchange='', routing_key='admin', body=event)
    connection.close()