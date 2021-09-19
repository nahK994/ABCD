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
        response = []
        for teacher in teachers:
            aa = {
                'teacherId': teacher.teacherId,
                'userName': teacher.userName,
                'name': teacher.name,
                'orgName': teacher.orgName,
                'aboutMe': teacher.aboutMe,
                'email': teacher.email
            }
            response.append(aa)
        return response
