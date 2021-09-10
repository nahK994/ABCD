from django.urls import path

from .views import *

urlpatterns = [
    path('teacher/', TeacherViewSet.as_view({
        'post': 'processEvent'
    })),
    path('teachers/', TeacherViewSet.as_view({
        'get': 'getList'
    })),
]
