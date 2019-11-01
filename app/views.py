from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"app/index.html")

def login(request):
    return render(request,"app/login.html")