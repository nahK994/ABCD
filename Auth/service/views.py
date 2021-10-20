from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Auth
from .eventPublisher import publish

class AuthViewSet(viewsets.ViewSet):
    def getAllEvents(self, request):
        users = Auth.objects.all()
        response = self.processResponse(users)
        return Response(response, status=status.HTTP_200_OK)
    
    def getEvent(self, request, pk):
        users = Auth.objects.filter(userId=pk)
        response = self.processResponse(users)
        return Response(response, status=status.HTTP_200_OK)
    
    def getUser(self, request):
        request = request.data
        user = Auth.objects.filter(email=request['email'], password=request['password'])
        queryResult = self.processResponse(user)

        if len(queryResult) == 0:
            return Response("Wrong email or password", status=status.HTTP_200_OK)
        else:
            return Response(queryResult[0]['userId'], status=status.HTTP_200_OK)


    def processEvent(self, request):
        data = request.data
        loginInfo = Auth(
            userId=data['userId'],
            email=data['email'],
            password=data['password'],
        )
        event = {
            'userId': data['userId'],
            'name': data['name'],
            'email': data['email'],
            'orgName': data['orgName'],
            'aboutMe': data['aboutMe']
        }

        users = Auth.objects.all()
        filterWithEmail = Auth.objects.filter(email=event['email'])

        if len(self.processResponse(filterWithEmail)) != 0:
            return Response("Email has already used", status=status.HTTP_400_BAD_REQUEST)

        loginInfo.save()
        publish(event)
        return Response(data['userId'], status=status.HTTP_201_CREATED)


    def processResponse(self, users):
        response = []
        for user in users:
            userInfo = {
                'userId': user.userId,
                'email': user.email,
                'password': user.password
            }
            response.append(userInfo)
        return response
