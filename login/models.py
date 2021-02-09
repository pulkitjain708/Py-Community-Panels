from django.db import models
from django.contrib.auth.models import User
from constants import UserTypes as ut , LoginStatus as lt , Activation as ac , Status as st , Gender as gd
# Create your models here.

class userAccount(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=15)
    role=models.CharField(
      max_length=12,
      choices=[(tag.value, tag.value) for tag in ut]  
    )
    loginStatus=models.CharField(
      max_length=12,
      choices=[(tag.value, tag.value) for tag in lt]  
    )
    status=models.CharField(
      max_length=12,
      choices=[(tag.value, tag.value) for tag in st]  
    )
    activation=models.CharField(
      max_length=12,
      choices=[(tag.value, tag.value) for tag in ac]  
    )
    dob=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(
      max_length=12,
      choices=[(tag.value,tag.value) for tag in gd]  
    )
    profile=models.ImageField(upload_to='images/')

   