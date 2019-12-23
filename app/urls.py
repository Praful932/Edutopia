from django.urls import path
from django.contrib.auth import views as auth_views
from app.views import (PostDetailView, PostListViewMentor,
                       PostUpdateView, PostDeleteView, Omega)
from . import views

# django.urls expects an app as an argument
# logoutf, loginf - to avoid name conflicts

urlpatterns = [
    path("", views.index, name='index'),
    path(r"register/", views.register, name='register'),
    path(r"omega/", Omega.as_view(), name='omega'),
    path(r"loginf/", auth_views.LoginView.as_view(
        template_name='app/login.html'), name='login'),
    path(r"password-reset/", auth_views.PasswordResetView.as_view(
        template_name='app/password_reset.html'), name='password_reset'),
    path(r"password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name='password_reset_done'),
    path(r"password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html'), name='password_reset_confirm'),
    path(r"password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    path(r"logoutf/", views.logoutf, name='logout'),
    path(r"registerStudent/", views.registerStudent, name='registerStudent'),
    path(r"registerMentor/", views.registerMentor, name='registerMentor'),
    path(r"MentorPost/", views.MentorPost, name='MentorPost'),
    path(r"alpha/", views.alpha, name='alpha'),
    path(r"AlphaAdd/", views.AlphaAdd, name='AlphaAdd'),
    path(r"beta/", views.beta, name='beta'),
    path(r"UpdateProfile/", views.UpdateProfile, name='UpdateProfile'),
    path(r"post/<int:pk>/", PostDetailView.as_view(), name='SinglePost'),
    path(r"myposts/", PostListViewMentor.as_view(), name='MyPosts'),
    path(r"post/<int:pk>/update/", PostUpdateView.as_view(), name='UpdatePost'),
    path(r"post/<int:pk>/delete/", PostDeleteView.as_view(), name='DeletePost')
]
