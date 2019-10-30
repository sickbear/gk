# coding=utf-8
from django.urls import path, include

from .views import article_detail, article_detail_amp, show_rubric
# from .views import show_rubric

urlpatterns = [
    path('rubric/<rubric_slug>/', show_rubric, name='content_show_rubric'),
    path('article/<article_slug>/amp/', article_detail_amp, name='content_show_article_amp'),
    path('article/<article_slug>/', article_detail, name='content_show_article'),
    # url(r'^(?P<article_slug>[a-zA-Z0-9\-+_.]+)/', article_detail, name=u'wiki_show_article'),
]