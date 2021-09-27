from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import TeacherCommand
from .eventPublisher import publish
import requests

class TeacherViewSet(viewsets.ViewSet):
    def getAllEvents(self, request):
        teachers = TeacherCommand.objects.all()
        response = []
        for teacher in teachers:
            aa = {
                'eventId': teacher.eventId,
                'userId': teacher.userId,
                'name': teacher.name,
                'orgName': teacher.orgName,
                'aboutMe': teacher.aboutMe,
                'email': teacher.email
            }
            response.append(aa)
        return Response(response, status=status.HTTP_200_OK)

    # def processEvent(self, request):
    #     data = request.data
    #     teacher = TeacherCommand(
    #         teacherId=data['teacherId'],
    #         userName=data['userName'],
    #         name=data['name'],
    #         email=data['email'],
    #         orgName=data['orgName'],
    #         aboutMe=data['aboutMe']
    #     )
    #     event = {
    #         'teacherId': data['teacherId'],
    #         'userName': data['userName'],
    #         'name': data['name'],
    #         'email': data['email'],
    #         'orgName': data['orgName'],
    #         'aboutMe': data['aboutMe']
    #     }
        
    #     responseFromQuery = requests.get('http://localhost:8001/teachers/')
    #     responseFromQuery = responseFromQuery.json()
    #     for response in responseFromQuery:
    #         if response['email'] == event['email'] or response['teacherId'] == event['teacherId'] or response['userName'] == event['userName']:
    #             return Response("username or email is already taken or something is wrong. Please try again", status=status.HTTP_400_BAD_REQUEST)

    #     publish(event)
    #     teacher.save()
    #     return Response(data['teacherId'], status=status.HTTP_201_CREATED)
