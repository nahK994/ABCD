from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacherId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    headline = models.CharField(max_length=40, unique=True)
    email = models.CharField(max_length=20, unique=True)
    createdCourses = models.ManyToManyField(int)
    createdTopics = models.ManyToManyField(int)
    assignedCourseList = models.ManyToManyField(int)