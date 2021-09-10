from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializers

class UserViewSet(viewsets.ViewSet):
    def getList(self, request):
        users = User.objects.all()
        response = []
        for user in users:
            aa = {
                'itemId': user.itemId,
                'email': user.email,
                'password': user.password,
                'userName': user.userName
            }
            response.append(aa)
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        user = User(itemId=data['itemId'], userName=data['userName'], email=data['email'], password=data['password'])
        user.save()
        return Response(data, status=status.HTTP_201_CREATED)

    def remove(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.delete()
        publish('user_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
