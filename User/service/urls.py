from django.urls import path

from .views import *

urlpatterns = [
    path('user/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
]
