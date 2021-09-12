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
                'teacherId': teacher.teacherId,
                'email': teacher.email,
                'password': teacher.password,
                'userName': teacher.userName
            }
            response.append(aa)
        return Response(response, status=status.HTTP_200_OK)

    def processEvent(self, request):
        data = request.data
        teacher = TeacherCommand(teacherId=data['teacherId'], userName=data['userName'], email=data['email'], password=data['password'])
        event = {
            'teacherId': data['teacherId'],
            'userName': data['userName'],
            'email': data['email'],
            'password': data['password']
        }
        
        responseFromQuery = requests.get('http://localhost:8001/teachers/')
        responseFromQuery = responseFromQuery.json()
        for response in responseFromQuery:
            if response['email'] == event['email'] or response['teacherId'] == event['teacherId']:
                return Response("username or email is already taken", status=status.HTTP_400_BAD_REQUEST)

        publish(event)
        teacher.save()
        return Response(data, status=status.HTTP_201_CREATED)
