from django.urls import path
from . import views

# django.urls expects an app as an argument

urlpatterns=[
    path("",views.index,name='home'),
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
    path("omega/",views.omega,name='omega')
]