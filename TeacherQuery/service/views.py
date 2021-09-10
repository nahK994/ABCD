from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import TeacherQuery

class TeacherViewSet(viewsets.ViewSet):
    def getList(self, request):
        print("response ===> ", request.data)
        return Response(status=status.HTTP_200_OK)
