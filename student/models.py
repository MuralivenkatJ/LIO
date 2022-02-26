from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from course.models import Course
from institute.models import Institute

# Create your models here.
class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    image = models.ImageField(upload_to='media/student', default='student/default.jpg')
    password = models.CharField(max_length=200)
    i_id = models.ForeignKey(Institute, on_delete=models.CASCADE)

    courses = models.ManyToManyField(Course, related_name='courses', through='Enrolls')
    ratings = models.ManyToManyField(Course, related_name='ratings', through='Rates')
    wished  = models.ManyToManyField(Course, related_name='wished', through='Wishlist')

    def __str__(self):
        return self.s_name

class Enrolls(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default='inprogress')
    watched = models.CharField(max_length=500, default='')

    class Meta:
        unique_together = [['s_id', 'c_id']]

class Rates(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    desc = models.TextField()

    class Meta:
        unique_together = [['s_id', 'c_id']]

class Wishlist(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['s_id', 'c_id']]

class Pays(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    utr_no = models.CharField(max_length=15)
    image = models.ImageField(upload_to='payment')
    date = models.DateField(default=datetime.date(datetime.now()))
    time = models.TimeField(default=datetime.time(datetime.now()))

    class Meta:
        unique_together = [['s_id', 'c_id']]