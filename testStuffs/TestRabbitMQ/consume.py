import pika

params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')

def callbackFunc(ch, methods, properties, body):
    print(body)

try:
    channel.basic_consume(queue='admin', on_message_callback=callbackFunc)

    channel.start_consuming()
except:
    channel.stop_consuming()
    print("ended")