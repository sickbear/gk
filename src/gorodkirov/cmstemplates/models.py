# coding=utf-8
from django.db import models


class TemplateFragment(models.Model):
    """html-шаблон для вставки на сайт."""
    name = models.CharField('Название шаблона', max_length=25, db_index=True)
    description = models.CharField('Описание шаблона', max_length=255, blank=True)
    text = models.TextField('Текст шаблона', blank=True, default='')

    class Meta:
        verbose_name = 'Файл шаблона'
        verbose_name_plural = 'Файлы шаблона'


class SiteLogo(models.Model):
    """Логотип сайта."""
    logo = models.ImageField('Логотип', upload_to='logo', blank=False, null=False)

    class Meta:
        verbose_name = 'Логотип сайта'
        verbose_name_plural = 'Логотипы сайта'


class NewSettings(models.Model):
    """Настройки новостей."""
    COUNT = [
        (1, 1,), (2, 2,), (3, 3,), (4, 4,), (5, 5,), (6, 6,), (7, 7,), (8, 8,), (9, 9,), (10, 10,)
    ]

    name = models.CharField('Название раздела', max_length=55, db_index=True)
    count = models.PositiveSmallIntegerField('Количество коммерч. статей', choices=COUNT)

    class Meta:
        verbose_name = 'Настройки новостей'
        verbose_name_plural = 'Настройки новостей'
