from django.urls import path
from . import views

# django.urls expects an app as an argument

urlpatterns=[
    path("",views.index)
]