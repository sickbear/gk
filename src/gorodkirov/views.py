# coding=utf-8
import json
from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import loader
from django.db.models import Q
from gorodkirov.users.forms import SignupForm
from gorodkirov.articles import queries as articles_queries
from gorodkirov.articles.models import Article


def homepage(request):
    """Отображает главную страницу."""
    main_news = articles_queries.get_main_news()
    operational_news = articles_queries.get_operational_news()
    big_block_1 = articles_queries.get_article_for_big_block_1()
    big_block_2 = articles_queries.get_article_for_big_block_2()
    big_block_3 = articles_queries.get_article_for_big_block_3()
    city_details = articles_queries.GetCityDetails()
    city_details.get_result()
    chronicle_rubrics = articles_queries.get_chronicle_rubrics()
    test_drive = articles_queries.get_test_drive()
    inner = False

    return render(request, 'homepage.html', {
        'form': SignupForm,
        'main_news': main_news,
        'operational_news': operational_news,
        'city_block_1': city_details.articles_block_1,
        'city_block_2': city_details.articles_block_2,
        'city_block_3': city_details.articles_block_3,
        'chronicle_rubrics': chronicle_rubrics,
        'test_drive': test_drive,
        'big_block_1': big_block_1,
        'big_block_2': big_block_2,
        'big_block_3': big_block_3,
        'inner': inner,
    })


def search(request):
    """Поиск по сайту."""
    if request.is_ajax:
        query = request.GET.get('q')
        if not query:
            return HttpResponse(json.dumps({'count': 0, 'results': []}), content_type='application/json; charset=UTF-8')

        articles = Article.objects.filter(active=True)
        terms = query.split()
        for term in terms:
            articles = articles.filter(Q(title__icontains=term)).order_by('-date_sort')
        articles = articles[:50]

        html = render_to_string('modals/includes/search_result.html', {'articles': articles})
        return HttpResponse(html)
