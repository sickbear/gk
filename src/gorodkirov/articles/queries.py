# coding=utf-8
from .models import Rubric, Article


def get_urgent_article():
    """Получает статью для раздела Срочно."""
    return Article.objects.filter(urgently=True).order_by('-date_sort')[:1]


# def get_rubrictree_for_news():
#     rubrics = Rubric.objects.get(name=u'Новости').get_descendants(include_self=True)
#
#     return rubrics
#
#
# def get_articles_for_slider(count):
#     rubrics = get_rubrictree_for_news()
#
#     articles = Article.objects.published().filter(
#         rubric__in=rubrics,
#         on_main=True,
#     ).order_by('-date_sort')[:count]
#
#     return articles
