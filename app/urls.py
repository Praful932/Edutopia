from django.urls import path
from django.contrib.auth import views as auth_views
from app.views import (PostDetailView,PostListView, 
    PostUpdateView, PostDeleteView)
from . import views

# django.urls expects an app as an argument

# logoutf, loginf - to avoid name conflicts

urlpatterns = [
    path("", views.index, name='index'),
    path(r"register", views.register, name='register'),
    path(r"omega", views.omega, name='omega'),
    path(r"loginf", auth_views.LoginView.as_view(
        template_name='app/login.html'), name='login'),
    path(r"logoutf", views.logoutf, name='logout'),
    path(r"registerStudent", views.registerStudent, name='registerStudent'),
    path(r"registerMentor", views.registerMentor, name='registerMentor'),
    path(r"MentorPost", views.MentorPost, name='MentorPost'),
    path(r"alpha", views.alpha, name='alpha'),
    path(r"AlphaAdd", views.AlphaAdd, name='AlphaAdd'),
    path(r"beta", views.beta, name='beta'),
    path(r"UpdateProfile", views.UpdateProfile, name='UpdateProfile'),
    path(r"post/<int:pk>",PostDetailView.as_view(),name='SinglePost'),
    path(r"myposts",PostListView.as_view(),name='MyPosts'),
    path(r"post/<int:pk>/update",PostUpdateView.as_view(),name='UpdatePost'),
    path(r"post/<int:pk>/delete",PostDeleteView.as_view(),name='DeletePost')
]

