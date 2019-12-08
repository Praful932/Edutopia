from django.shortcuts import render, redirect
from app.forms import StudentSignUpForm, StudentFieldForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login

# commit = False used when before saving it is needed to input any other data or associated any other model

# Create your views here.
def index(request):
    return render(request,"app/index.html")

def loginf(request):
    return render(request,"app/login.html")

def register(request):
    if(request.method=="GET"):
        return render(request,"app/register.html") 

def omega(request):
    return render(request,"app/omega.html")

def registerStudent(request):
    if request.method=='POST':
        # Create form instance with POST data
        signupform = StudentSignUpForm(request.POST)
        studentform = StudentFieldForm(request.POST)
        if signupform.is_valid() and studentform.is_valid():
            username = signupform.cleaned_data.get('username')
            new_user = signupform.save(commit=False)
            new_user.is_student = True
            new_user = signupform.save()
            # login the new registered user
            login(request, new_user)
            student=studentform.save(commit=False)
            student.user = new_user
            studentform.save()
            messages.success(request,f'Account successfully created for {username}!')
            return redirect('index')
    else:
        signupform = StudentSignUpForm()
        studentform = StudentFieldForm()
    context={
    'signupform' : signupform ,
    'studentform' : studentform
    }
    return render(request,"app/registerstudent.html",context=context)

def logoutf(request):
    # Check if user is logged in if not redirect to login page
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.success(request,f'Successfully Logged out {username}!')
        return redirect('index')
    return redirect('login')
        

