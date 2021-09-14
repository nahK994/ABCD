from django.db import models

class TeacherQuery(models.Model):
    teacherId = models.CharField(primary_key=True, unique=True, max_length=20)
    userName = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
