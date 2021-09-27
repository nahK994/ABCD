from django.db import models

class TeacherQuery(models.Model):
    userId = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    orgName = models.CharField(max_length=40)
    aboutMe = models.CharField(max_length=80)
    email = models.CharField(max_length=20)
