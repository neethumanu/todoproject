from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dtm

# Create your models here.
class Register(models.Model):
    
# user details
    Users = models.OneToOneField(User,on_delete=models.CASCADE)
    Phone_number = models.CharField(max_length=10)
    Address = models.CharField(max_length=100)
    DOB = models.DateField(auto_created=False,auto_now=False)
    DOJ = models.DateTimeField(auto_created=False,auto_now=False,default=dtm.now)
    Image = models.ImageField('media')
