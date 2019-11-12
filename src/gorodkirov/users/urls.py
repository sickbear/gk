# coding=utf-8
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.show_profile, name='show_profile'),
    path('read/', views.show_read, name='show_read'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('password-change/', views.password_change, name='password_change'),
]
