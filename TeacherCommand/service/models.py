from django.db import models

class TeacherCommand(models.Model):
    eventId = models.AutoField(primary_key=True)
    teacherId = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    orgName = models.CharField(max_length=40)
    aboutMe = models.CharField(max_length=80)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
