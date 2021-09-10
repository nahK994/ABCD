from django.urls import path

from .views import *

urlpatterns = [
    path('user/<str:pk>/', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'remove'
    })),
    path('user/', UserViewSet.as_view({
        'post': 'create'
    })),
    path('users/', UserViewSet.as_view({
        'get': 'getList'
    })),
]
