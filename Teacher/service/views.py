from django.shortcuts import render
from .models import *
from rest_framework import viewsets


class TeacherViewSet(viewsets.ViewSet):
    
    def list(self, request):
        print("<-------------calling teacher service----------->")
