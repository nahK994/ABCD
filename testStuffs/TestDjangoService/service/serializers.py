from rest_framework import serializers
from .models import *

class UserSerializers(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'