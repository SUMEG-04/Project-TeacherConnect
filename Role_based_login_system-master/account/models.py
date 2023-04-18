from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_subadmin = models.BooleanField('Is subadmin', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)

class Database(models.Model):
    EmpID = models.IntegerField(max_length=25)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    college = models.CharField(max_length=50)
    subject = models.CharField(max_length=30)
    designation = models.CharField(max_length=40)
    # is_phD = models.BooleanField('is phd',default = True)
    



