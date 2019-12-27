from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import User, Student, Mentor, Domain, Post, Message

# (Student/Mentor)SignUpForm - UserCreationForm for Student or Mentor
# (Student/Mentor)FieldForm - ModelForm for Student or Mentor


class StudentSignUpForm(UserCreationForm):
    class Meta():
        fields = ['username', 'email', 'password1', 'password2']
        model = User


class StudentFieldForm(forms.ModelForm):
    class Meta():
        fields = ['domain', 'proficiency','OtherInfo']
        model = Student
        labels = {
            'OtherInfo': 'Other Info'
        }


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

# Both for Student and Mentor
class UserUpdateForm(forms.ModelForm):
    class Meta():
        fields = ['username','email']
        model = User

class SendMessage(forms.ModelForm):
    class Meta():
        fields =['receiver','msg_content']
        model = Message
        labels ={
            'receiver' : 'Send To',
            'msg_content' : 'Type your Message here'
        }
    
    def __init__(self,*args,**kwargs):
        # catch passed in user and pop it to exclude receiver object
        current_user = kwargs.pop('current_user')
        super(SendMessage, self).__init__(*args, **kwargs)
        username_to_exclude = [current_user.username,'admin']
        # self.fields['receiver'].queryset = User.objects.exclude(username=self.user.username)
        self.fields['receiver'].queryset = User.objects.exclude(username__in = username_to_exclude)
