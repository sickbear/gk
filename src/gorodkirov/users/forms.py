from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1')
