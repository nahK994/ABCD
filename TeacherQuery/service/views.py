from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import TeacherQuery

class TeacherViewSet(viewsets.ViewSet):
    def retrieveAll(self, request):
        teachers = TeacherQuery.objects.all()
        response = self.processResponse(teachers)
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        teacher = TeacherQuery.objects.filter(teacherId=pk)
        response = self.processResponse(teacher)
        return Response(response, status=status.HTTP_200_OK)

    def processResponse(self, teachers):
        print("process")
        response = []
        for teacher in teachers:
            aa = {
                'teacherId': teacher.teacherId,
                'email': teacher.email,
                'userName': teacher.userName
            }
            response.append(aa)
        return response
