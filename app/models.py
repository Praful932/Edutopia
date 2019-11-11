from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_mentor  = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    interests = models.ManyToManyField()
