# coding=utf-8
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from .tokens import account_activation_token
from .forms import SignupForm, ProfileForm
from .models import Profile


def json_response(x):
    """Формирование JSON-ответа."""
    return HttpResponse(json.dumps(x, sort_keys=True, indent=2), content_type='application/json; charset=UTF-8')


def register(request):
    """Регистрация нового пользователя.

    Получает регистрационные данные нового пользователя
    и отправляет письмо подтверждения email.
    Регестрирует пользователя в базе (auth_user: is_active=False).
    """
    if request.is_ajax:
        post_dict = request.POST.copy()
        post_dict['password2'] = post_dict['password1']
        form = SignupForm(post_dict)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Активация аккаунта на Gorodkirov.ru'
            from_email = settings.EMAIL_HOST_USER
            to_email = []
            to_email.insert(0, form.cleaned_data.get('email'))
            send_mail(mail_subject, message, from_email, to_email, fail_silently=False)

            template = loader.get_template('modals/includes/registration_success.html')
            template_html = template.render()
            return json_response({'success': True, 'html': template_html})
        else:
            return json_response({'success': False, 'errors': form.errors})

    return redirect('homepage')


def activate(request, uidb64, token):
    """Активирует пользователя после подтверждения email (auth_user: is_active=True)."""
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('homepage')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required
def show_profile(request):
    """Отображает аккаунт пользователя с закладками.
    В POST принимает и валидирует данные сохраняемого профиля.
    """
    response = render(request, 'users/includes/bookmarks.html', {})

    if request.POST:
        form = ProfileForm(request.POST)

        if form.is_valid():
            # user.profile.phone =
            pass
        else:
            print('form is NOT valid!!!!')
            response = render(request, 'users/includes/edit_profile.html', {'form': form})

    return response


@login_required
def show_read(request):
    """Отображает аккаунт пользователя с прочитанными новостями."""
    return render(request, 'users/includes/read_news.html', {})


@login_required
def edit_profile(request):
    """Отображает страницу редактирования профиля."""
    return render(request, 'users/includes/edit_profile.html', {})
