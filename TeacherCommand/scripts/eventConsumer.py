import pika
import json
from service.models import TeacherCommand


def run():
    def callbackFunc(ch, methods, properties, body):
        body = body.decode('ASCII')
        data = json.loads(body)
        print(data, type(data))
        teacher = TeacherCommand(
            userId=data['userId'],
            name=data['name'],
            email=data['email'],
            orgName=data['orgName'],
            aboutMe=data['aboutMe']
        )
        
        try:
            teacher.save()
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='login', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='login', queue=queue_name)
    try:
        channel.basic_consume(queue=queue_name, on_message_callback=callbackFunc, auto_ack=True)
        channel.start_consuming()
    except:
        channel.close()
        connection.close()
        print("ended")