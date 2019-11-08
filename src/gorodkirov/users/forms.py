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
    phone = forms.CharField(max_length=15)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone'].error_messages = {'required': 'Неверно введён номер телефона.'}

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone is None:
            raise forms.ValidationError()
        return phone
