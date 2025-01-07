from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=29)
    qualification = models.CharField(max_length=30)
    age = models.IntegerField()
    course = models.CharField(max_length=28)
    gender = models.CharField(max_length=20)
    skills = models.CharField(max_length=50)
    mock_rating = models.IntegerField()


     