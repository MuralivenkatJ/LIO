import email
from email.mime import image
from tkinter import CASCADE
from django.db import models

from institute.models import Institute

# Create your models here.
class Faculty(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=50)
    email = models.EmailField()
    qualification = models.TextField()
    image = models.ImageField(upload_to='faculty')
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=200)
    i_id = models.ForeignKey(Institute, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default="Pending")

    def __str__(self):
        return self.f_name