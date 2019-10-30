# coding=utf-8
from django.shortcuts import render
from gorodkirov.users.forms import SignupForm

from gorodkirov.articles import queries as articles_queries


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
    })


def timeline(request):
    """Отображает ленту новостей."""
    pass
