import pika
import json
from service.models import TeacherQuery


def run():
    def callbackFunc(ch, methods, properties, body):
        body = body.decode('ASCII')
        data = json.loads(body)
        print(data, type(data))
        teacher = TeacherQuery(teacherId=data['teacherId'], userName=data['userName'], email=data['email'], password=data['password'])
        teacher.save()

    params = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='admin')
    try:
        channel.basic_consume(queue='admin', on_message_callback=callbackFunc)
        channel.start_consuming()
    except:
        channel.close()
        connection.close()
        print("ended")