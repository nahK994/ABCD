import pika
import json

def publish(event):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    event = json.dumps(event)
    channel.exchange_declare(exchange='login', exchange_type='fanout')
    channel.basic_publish(exchange='login', routing_key='', body=event)
    connection.close()