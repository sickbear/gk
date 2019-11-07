# coding=utf-8
from django.contrib import admin
from django.db import models
from django.forms import Textarea
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from .models import TemplateFragment, SiteLogo, NewSettings


@register(TemplateFragment)
class TemplateFragmentAdmin(MaterialModelAdmin):
    list_display = ['name', 'description']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 30, 'cols': 150})},
    }


@register(SiteLogo)
class LogoAdmin(MaterialModelAdmin):
    list_display = ['logo']


@register(NewSettings)
class NewSettingsAdmin(MaterialModelAdmin):
    list_display = ['name']
