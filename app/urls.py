from django.urls import path
from . import views

# django.urls expects an app as an argument

urlpatterns=[
    path("",views.index,name='index'),
    path(r"login",views.login,name='login'),
    path(r"register",views.register,name='register'),
    path(r"omega",views.omega,name='omega'),
    path(r"registerStudent",views.registerStudent,name='registerStudent')
]