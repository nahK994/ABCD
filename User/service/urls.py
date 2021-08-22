from django.urls import path

from .views import *

urlpatterns = [
    path('users', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('user/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
