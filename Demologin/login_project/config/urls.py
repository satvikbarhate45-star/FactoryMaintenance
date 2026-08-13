from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("home/", views.home, name="home"),
]