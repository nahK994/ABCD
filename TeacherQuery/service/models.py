from django.db import models

class TeacherQuery(models.Model):
    teacherId = models.IntegerField(primary_key=True, unique=True)
    userName = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
