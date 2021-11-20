from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import TeacherQuery
import jwt
from datetime import datetime
from dateutil.relativedelta import relativedelta

class TeacherViewSet(viewsets.ViewSet):
    def retrieveAll(self, request):
        teachers = TeacherQuery.objects.all()
        response = self.processResponse(teachers)
        return Response(response, status=status.HTTP_200_OK)

    def checkAuthorization(self, request, pk):
        try:
            token = request.headers['Authorization'].split()[1]
            tokenJSON = jwt.decode(token, "secret", algorithms=["HS256"])
            currentTime = datetime.now()
            expiryTime = datetime.strptime(tokenJSON['expiryTime'], '%m/%d/%Y, %H:%M:%S')
            if currentTime < expiryTime:
                return self.retrieve(pk)
            else:
                return Response('', status=status.HTTP_403_FORBIDDEN)
        except:
            return Response('', status=status.HTTP_401_UNAUTHORIZED)
    
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
