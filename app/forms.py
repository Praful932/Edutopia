from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import User,Student,Mentor

class StudentSignUpForm(forms.ModelForm):
    class Meta():
        model=User

        
