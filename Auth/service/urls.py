from django.urls import path

from .views import *

urlpatterns = [
    path('teacher/create/', AuthViewSet.as_view({
        'post': 'processEvent'
    })),
    path('credentials/', AuthViewSet.as_view({
        'get': 'getAllEvents'
    })),
    path('credential/<str:pk>/', AuthViewSet.as_view({
        'get': 'getEvent'
    }))
]