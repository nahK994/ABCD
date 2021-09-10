import pika

params = pika.URLParameters('amqps://ckhrcudq:5UX_xu5WBtdNWUtMUQFEOgqf2cTI7b-w@beaver.rmq.cloudamqp.com/ckhrcudq')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(event):
    print(event)
    channel.basic_publish(exchange='', routing_key='admin', body=event)