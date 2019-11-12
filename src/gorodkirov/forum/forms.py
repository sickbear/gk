# coding=utf-8
from django import forms
from .models import Thread, Post, Category, Section


class PostForm(forms.ModelForm):
    """Форма комментария."""

    class Meta:
        model = Post
        exclude = ['user', 'user_ip', 'thread', 'date_created', 'last_updated']
