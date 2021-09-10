from django.db import models

class User(models.Model):
    itemId = models.IntegerField(primary_key=True, unique=True)
    userName = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
