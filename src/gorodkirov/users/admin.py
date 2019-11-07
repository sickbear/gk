# coding=utf-8
from django.contrib import admin
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from .models import Profile


@register(Profile)
class ProfileAdmin(MaterialModelAdmin):
    model = Profile
    list_display = ('user', )
    raw_id_fields = ('user', )
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')



