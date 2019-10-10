# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(u'Аватар', upload_to='avatars', blank=True, null=True)

    class Meta:
        verbose_name = u'Профиль'
        verbose_name_plural = u'Профили'

    def __str__(self):
        return self.user.username
