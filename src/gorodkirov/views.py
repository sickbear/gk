# coding=utf-8
from django.shortcuts import render
from gorodkirov.users.forms import SignupForm

# from gorodkirov.articles import queries


def homepage(request):
    """Главная страница."""
    # articles = queries.get_articles_for_slider(5)
    # news = get_details()

    return render(request, 'homepage.html', {
        # 'articles': articles,
        # 'news': news,
        'form': SignupForm
    })
