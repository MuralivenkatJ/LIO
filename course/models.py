from datetime import date
from email.policy import default
from django.db import models
from faculty.models import Faculty

# Create your models here.
class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    level = models.CharField(max_length=30, default='Beginners')
    image = models.ImageField(upload_to='course')
    playlistid = models.CharField(max_length=40)
    duration = models.CharField(max_length=10)
    price = models.IntegerField()
    guided_project = models.BooleanField(default=False)
    description = models.CharField(max_length=600)
    date = models.DateField()
    total_views = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    f_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.c_name

class Course_skills(models.Model):
    id = models.AutoField(primary_key=True)
    skills = models.CharField(max_length=50)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE)