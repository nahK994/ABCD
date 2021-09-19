from django.db import models

class TeacherQuery(models.Model):
    teacherId = models.CharField(primary_key=True, max_length=20)
    userName = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    orgName = models.CharField(max_length=40)
    aboutMe = models.CharField(max_length=80)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
