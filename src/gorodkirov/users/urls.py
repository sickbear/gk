# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_profile, name='show_profile'),
    path('read/', views.show_read, name='show_read'),
    path('edit/', views.edit_profile, name='edit_profile'),
]
