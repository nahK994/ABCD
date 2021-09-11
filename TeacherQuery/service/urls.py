from django.urls import path

from .views import *

urlpatterns = [
    path('teachers/', TeacherViewSet.as_view({
        'get': 'retrieveAll'
    })),
    path('teacher/<int:pk>', TeacherViewSet.as_view({
        'get': 'retrieve'
    })),
]
