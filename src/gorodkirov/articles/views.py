# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


def show_rubric(request, rubric_slug):
    HttpResponse('Это рубрика!')


def article_detail(request, article_slug):
    HttpResponse('Это статья!')


def article_detail_amp(request, article_slug):
    HttpResponse('Это amp-статья!')
