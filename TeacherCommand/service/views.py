from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Teacher

class TeacherViewSet(viewsets.ViewSet):
    def getList(self, request):
        teachers = Teacher.objects.all()
        response = []
        for teacher in teachers:
            aa = {
                'itemId': teacher.itemId,
                'email': teacher.email,
                'password': teacher.password,
                'userName': teacher.userName
            }
            response.append(aa)
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        teacher = Teacher(itemId=data['itemId'], userName=data['userName'], email=data['email'], password=data['password'])
        teacher.save()
        return Response(data, status=status.HTTP_201_CREATED)
