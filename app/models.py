from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_mentor=models.BooleanField(default=False)
    role=models.CharField('Current Role',max_length=255)
    domains=models.CharField('Domain',max_length=255)

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class Mentor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class Post(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    # domains=models.
    


    


