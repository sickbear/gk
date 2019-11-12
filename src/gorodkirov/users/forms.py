# coding=utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from .models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1')


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    email = forms.CharField()
    phone = forms.CharField(max_length=15, required=False)
    city = forms.CharField(max_length=30)
    sex = forms.CharField(max_length=6)
    birthday = forms.DateTimeField(required=False)









