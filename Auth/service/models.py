from django.db import models

class Auth(models.Model):
    userId = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=40)
