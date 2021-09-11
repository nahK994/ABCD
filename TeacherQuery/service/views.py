from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import TeacherQuery

class TeacherViewSet(viewsets.ViewSet):
    def retrieveAll(self, request):
        teachers = TeacherQuery.objects.all()
        response = []
        for teacher in teachers:
            aa = {
                'teacherId': teacher.teacherId,
                'email': teacher.email,
                'password': teacher.password,
                'userName': teacher.userName
            }
            response.append(aa)
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        teacher = TeacherQuery.objects.filter(teacherId=pk)
        response = {
            'teacherId': teacher.teacherId,
            'email': teacher.email,
            'password': teacher.password,
            'userName': teacher.userName
        }
        return Response(response, status=status.HTTP_200_OK)
