from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import User, Student, Mentor, Domain, Post

# (Student/Mentor)SignUpForm - UserCreationForm for Student or Mentor
# (Student/Mentor)FieldForm - ModelForm for Student or Mentor


class StudentSignUpForm(UserCreationForm):
    class Meta():
        fields = ['username', 'email', 'password1', 'password2']
        model = User


class StudentFieldForm(forms.ModelForm):
    class Meta():
        fields = ['domain', 'proficiency']
        model = Student


class MentorSignUpForm(UserCreationForm):
    class Meta():
        fields = ['username', 'email', 'password1', 'password2']
        model = User


class MentorFieldForm(forms.ModelForm):
    domains = forms.ModelMultipleChoiceField(queryset=Domain.objects.all(),widget=forms.CheckboxSelectMultiple,required=True)
    class Meta():
        fields = ['domains','OtherInfo']
        model = Mentor
        labels = {
            'OtherInfo': 'Other Info'
        }

class MentorPostForm(forms.ModelForm):
    class Meta():
        fields =['topic','content','domain']
        model = Post

class LocForm(forms.ModelForm):
    class Meta():
        fields = ['lat','lng']
        model = User