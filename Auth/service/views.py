from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Auth
from .eventPublisher import publish

import random

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class AuthViewSet(viewsets.ViewSet):

    def getAllEvents(self, request):
        users = Auth.objects.all()
        response = self.processResponse(users)
        return Response(response, status=status.HTTP_200_OK)
    
    def getEvent(self, request, pk):
        users = Auth.objects.filter(userId=pk)
        response = self.processResponse(users)
        return Response(response, status=status.HTTP_200_OK)
    
    def loginUser(self, request):
        request = request.data
        user = Auth.objects.filter(email=request['email'], password=request['password'])
        queryResult = self.processResponse(user)

        response = self.createLoginInfo(queryResult[0]['userId'])

        if len(queryResult) == 0:
            return Response("Wrong email or password", status=status.HTTP_200_OK)
        else:
            return Response(response, status=status.HTTP_200_OK)
    
    def logoutUser(self, request):
        refreshToken = request.data
        cache.delete(refreshToken)
        return Response("", status=status.HTTP_200_OK)


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

        response = self.createLoginInfo(data['userId'])
        return Response(response, status=status.HTTP_201_CREATED)
    
    def createLoginInfo(self, userId):
        tokens = self.loginTokens()
        response = {
            'userId': userId,
            'accessToken': tokens['accessToken'],
            'refreshToken': tokens['refreshToken']
        }
        return response
    
    def loginTokens(self):
        refreshToken = random.randint(0, 1000)
        accessToken = 25*random.randint(0, 1000)
        cache.set(refreshToken, accessToken)
        tokens = {
            'accessToken': cache.get(refreshToken),
            'refreshToken': refreshToken
        }
        print("caching worked ", tokens)

        return tokens

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

    def refreshAccessToken(self, request):
        refreshToken = request.data
        if cache.get(refreshToken):
            cache.delete(refreshToken)
            tokens = self.loginTokens()
            return Response(tokens, status=status.HTTP_200_OK)
        else:
            return Response("", status=status.HTTP_200_OK)