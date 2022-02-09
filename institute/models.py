from django.db import models

# Create your models here.
class Institute(models.Model):
    i_id = models.AutoField(primary_key=True)
    i_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='institute')
    email = models.EmailField()
    website = models.CharField(max_length=50)
    ac_no = models.CharField(max_length=20)
    ac_name = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=20)
    b_name = models.CharField(max_length=30)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.i_name