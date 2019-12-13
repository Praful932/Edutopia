from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.utils import timezone
# Create your models here.

# on_delete=models.CASCADE when a foreign key's table is deleted delete all records if any associated with it
# using related name(defined in class a) it is possible to access all the objects related in class a from class b
# using blank=True makes to user associated with no domains
# The first item in the (tuple) is the value and second is the label to be shown on the radio button
# metadata ordering can be used to control default ordering of records'
class User(AbstractUser):
    is_student=models.BooleanField('student status',default=False)
    is_mentor=models.BooleanField('mentor status',default=False)
    lat=models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    lng=models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    def __str__(self):
        return self.username

class Domain(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    domaintrack=models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    level=(
        ('beg','Beginner'),
        ('inter','Intermediate'),
        ('exp','Expert')
        )
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    domain=models.OneToOneField(Domain,on_delete=models.CASCADE)
    proficiency=models.CharField(max_length=5,choices=level,default="beg") 

    def __str__(self):
        return self.user.username + ' - Student'
    

class Mentor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    domains=models.ManyToManyField(Domain,blank=False,related_name="experts")
    OtherInfo=models.TextField(max_length=200, help_text="Your Github/Portfolio Page or Anything you would like to add")
    
    def __str__(self):
        return self.user.username + ' (Mentor)'


class Post(models.Model):
    topic=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    created_at=models.DateTimeField(default = timezone.now)
    last_updated=models.DateTimeField(auto_now=True)
    domain=models.ForeignKey(Domain,on_delete=models.CASCADE,related_name="topicposts")
    owner=models.ForeignKey(Mentor,on_delete=models.CASCADE,related_name="postsby")

    def gist(self):
        return self.content[:20] + '...'

    def __str__(self):
        return self.topic + f'- {self.owner}'




