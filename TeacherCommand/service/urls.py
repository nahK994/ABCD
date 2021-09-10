from django.urls import path

from .views import *

urlpatterns = [
    path('teacher/', TeacherViewSet.as_view({
        'post': 'create'
    })),
    path('teachers/', TeacherViewSet.as_view({
        'get': 'getList'
    })),
]
