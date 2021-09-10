import pika

params = pika.URLParameters('amqps://ckhrcudq:5UX_xu5WBtdNWUtMUQFEOgqf2cTI7b-w@beaver.rmq.cloudamqp.com/ckhrcudq')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')

def callbackFunc(ch, methods, properties,  body):
    pass

channel.basic_consume(queue='admin', on_message_callback=callbackFunc)

channel.start_consuming()

channel.stop_consuming()

channel.close()