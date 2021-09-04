from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    organization = models.CharField(max_length=20)
