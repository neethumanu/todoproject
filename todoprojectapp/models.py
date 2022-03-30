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

    def __str__(self):
        return self.Users.username

class todo(models.Model):
    User_details = models.ForeignKey(Register,on_delete=models.CASCADE,related_name = 'todo')
    Title = models.CharField(max_length=100,blank=True,null=True)
    Content = models.TextField()
    Create_time = models.DateTimeField(auto_now=False,auto_now_add=False,default=dtm.now)
    Completed = models.BooleanField(default=False)
    Completition_date = models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)

    def __str__(self):
        return self.Title + ' | ' + self.User_details.Users.username