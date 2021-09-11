import pika

params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')
channel.basic_publish(exchange='', routing_key='admin', body='angry birds')
connection.close()
