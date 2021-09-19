import pika
import json
from service.models import TeacherQuery


def run():
    def callbackFunc(ch, methods, properties, body):
        body = body.decode('ASCII')
        data = json.loads(body)
        print(data, type(data))
        teacher = TeacherQuery(
            teacherId=data['teacherId'],
            userName=data['userName'],
            name=data['name'],
            email=data['email'],
            orgName=data['orgName'],
            aboutMe=data['aboutMe'],
            password=data['password']
        )
        
        try:
            teacher.save()
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

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