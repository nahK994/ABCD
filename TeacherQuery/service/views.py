from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import TeacherQuery

class TeacherViewSet(viewsets.ViewSet):
    def retrieveAll(self, request):
        teachers = TeacherQuery.objects.all()
        response = self.processResponse(teachers)
        return Response(response, status=status.HTTP_200_OK)

    def checkAuthorization(self, request, pk):
        if request.headers['Authorization'].split()[1] != "25":
            return Response('', status=status.HTTP_401_UNAUTHORIZED)
        else:
            return self.retrieve(pk)
    
    def retrieve(self, pk):
        teacher = TeacherQuery.objects.filter(userId=pk)
        response = self.processResponse(teacher)
        return Response(response, status=status.HTTP_200_OK)

    def processResponse(self, teachers):
        response = []
        for teacher in teachers:
            teacherInfo = {
                'userId': teacher.userId,
                'name': teacher.name,
                'orgName': teacher.orgName,
                'aboutMe': teacher.aboutMe,
                'email': teacher.email
            }
            response.append(teacherInfo)
        return response
