# coding=utf-8
from django.shortcuts import get_object_or_404
from .models import Profile


def profile(request):
    """Получает данные пользователя."""
    user = request.user
    if user.is_active:
        profile = get_object_or_404(Profile, user_id=user.id)
        return {
            'user_name': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'avatar': profile.avatar,
            'phone': profile.phone,
            'city': profile.city,
            'sex': profile.sex,
            'birthday': profile.birthday
        }
    else:
        return {
            'user_name': 'Аноним',
            'avatar': None
        }
