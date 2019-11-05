# coding=utf-8
from django.urls import path, include
from . import views


urlpatterns = [
    path('rubric/<rubric_slug>/', views.show_rubric, name='content_show_rubric'),
    path('article/<article_slug>/amp/', views.article_detail_amp, name='content_show_article_amp'),
    path('article/<article_slug>/', views.article_detail, name='content_show_article'),
    # url(r'^(?P<article_slug>[a-zA-Z0-9\-+_.]+)/', views.article_detail, name=u'wiki_show_article'),
]
