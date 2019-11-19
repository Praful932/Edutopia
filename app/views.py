from django.shortcuts import render

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