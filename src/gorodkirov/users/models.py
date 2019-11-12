# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Расширенная модель пользователя."""
    GENDER_CHOICES = (('male', 'мужской'), ('female', 'женский'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар', upload_to='avatars', blank=True, null=True)
    phone = models.CharField('Телефон', max_length=15, blank=True)
    city = models.CharField('Город', max_length=30, blank=True)
    sex = models.CharField('Пол', max_length=6, choices=GENDER_CHOICES, default='male')
    birthday = models.DateTimeField('День рождения', blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
