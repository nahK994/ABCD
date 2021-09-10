from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import TeacherCommand

class TeacherViewSet(viewsets.ViewSet):
    def getList(self, request):
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

    def create(self, request):
        data = request.data
        teacher = TeacherCommand(teacherId=data['teacherId'], userName=data['userName'], email=data['email'], password=data['password'])
        teacher.save()
        return Response(data, status=status.HTTP_201_CREATED)
