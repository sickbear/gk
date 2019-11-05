# coding=utf-8
from django.shortcuts import render, get_object_or_404
from gorodkirov.articles import queries as articles_queries
from .models import Article, Rubric


def timeline(request):
    """Отображает ленту новостей."""
    articles = Article.objects.filter(active=True)
    big_block_1 = articles_queries.get_article_for_big_block_1()
    big_block_2 = articles_queries.get_article_for_big_block_2()
    big_block_3 = articles_queries.get_article_for_big_block_3()
    chronicle_rubrics = articles_queries.get_chronicle_rubrics()
    test_drive = articles_queries.get_test_drive()
    inner = True

    return render(request, 'articles/news_feed.html', {
        'articles': articles,
        'label': 'Лента новостей',
        'big_block_1': big_block_1,
        'big_block_2': big_block_2,
        'big_block_3': big_block_3,
        'chronicle_rubrics': chronicle_rubrics,
        'test_drive': test_drive,
        'inner': inner,
    })


def show_rubric(request, rubric_slug):
    """Отображает все статьи рубрики."""
    rubric = get_object_or_404(Rubric, slug=rubric_slug)
    articles = Article.objects.filter(active=True, rubric=rubric)
    big_block_1 = articles_queries.get_article_for_big_block_1()
    big_block_2 = articles_queries.get_article_for_big_block_2()
    big_block_3 = articles_queries.get_article_for_big_block_3()
    chronicle_rubrics = articles_queries.get_chronicle_rubrics()
    test_drive = articles_queries.get_test_drive()
    inner = True

    return render(request, 'articles/news_feed.html', {
        'articles': articles,
        'label': rubric,
        'big_block_1': big_block_1,
        'big_block_2': big_block_2,
        'big_block_3': big_block_3,
        'chronicle_rubrics': chronicle_rubrics,
        'test_drive': test_drive,
        'inner': inner,
    })


def articles_by_tags(request):
    """Отображает статьи по тегу."""
    tag = request.GET.get('t', '')
    articles = Article.objects.filter(active=True, tags__text=tag)
    big_block_1 = articles_queries.get_article_for_big_block_1()
    big_block_2 = articles_queries.get_article_for_big_block_2()
    big_block_3 = articles_queries.get_article_for_big_block_3()
    chronicle_rubrics = articles_queries.get_chronicle_rubrics()
    test_drive = articles_queries.get_test_drive()
    inner = True

    return render(request, 'articles/news_feed.html', {
        'articles': articles,
        'label': '#{}'.format(tag),
        'big_block_1': big_block_1,
        'big_block_2': big_block_2,
        'big_block_3': big_block_3,
        'chronicle_rubrics': chronicle_rubrics,
        'test_drive': test_drive,
        'inner': inner,
    })


def article_detail(request, article_slug):
    """Отображает статью."""
    article = get_object_or_404(Article, slug=article_slug)
    return render(request, 'articles/new_article.html', {'article': article})


def article_detail_amp(request, article_slug):
    """Отображает amp-версию статьи."""
    pass
