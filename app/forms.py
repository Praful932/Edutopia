from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import User,Student,Mentor,Domain

# (Student/Mentor)SignUpForm - UserCreationForm for Student or Mentor
# (Student/Mentor)FieldForm - ModelForm for Student or Mentor

class StudentSignUpForm(UserCreationForm):
    class Meta():
        fields=['username','email','password1','password2']
        model=User 
        
class StudentFieldForm(forms.ModelForm):
    class Meta():
        fields=['domain','proficiency']
        model=Student