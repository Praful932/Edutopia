from django.shortcuts import render
from app.forms import StudentSignUpForm,StudentFieldForm
# Create your views here.
def index(request):
    return render(request,"app/index.html")

def login(request):
    return render(request,"app/login.html")

def register(request):
    if(request.method=="GET"):
        return render(request,"app/register.html") 

def omega(request):
    return render(request,"app/omega.html")

def registerStudent(request):
    if request.method == 'GET':
        signupform = StudentSignUpForm()
        studentform = StudentFieldForm()
        context={
            'signupform':signupform,
            'studentform':studentform
        }

    return render(request,"app/registerstudent.html",context=context)


