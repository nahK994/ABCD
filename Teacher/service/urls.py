from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('teacher/', views.TeacherViewSet.as_view({
        "get": "list"
    })),
]
