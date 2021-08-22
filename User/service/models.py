from django.db import models

class User(models.Model):
    itemId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
