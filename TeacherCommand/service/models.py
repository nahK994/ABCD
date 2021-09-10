from django.db import models

class TeacherCommand(models.Model):
    eventId = models.AutoField(primary_key=True)
    teacherId = models.IntegerField()
    userName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
