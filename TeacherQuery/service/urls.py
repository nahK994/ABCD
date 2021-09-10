from django.urls import path

from .views import *

urlpatterns = [
    path('teachers/', TeacherViewSet.as_view({
        'get': 'getList'
    })),
]
