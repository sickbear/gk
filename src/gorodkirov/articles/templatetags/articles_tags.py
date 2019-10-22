# coding: utf-8

# import feedparser
import random
from django import template
#
# from .. import models as m
from .. import queries as articles_queries
#
#
register = template.Library()
#
#
# @register.assignment_tag()
# def get_rubrics():
#     news_rubric = m.Rubric.objects.get(name=u'Новости')
#     return news_rubric.get_descendants().select_related('articles').all()


@register.simple_tag()
def get_urgent_article():
    """Отображает статью в разде Срочно."""
    return articles_queries.get_urgent_article()

# @register.assignment_tag()
# def get_popular_tags():
#     return m.PopularTag.objects.filter(rubric__isnull=True)
#
#
#
# @register.assignment_tag()
# def get_popular_tags_for_rubric(rubric):
#     return m.PopularTag.objects.filter(rubric=rubric)
#
#
# @register.assignment_tag()
# def get_medianethrics_entry():
#     feed = feedparser.parse('https://mediametrics.ru/partner/inject/online.ru.rss')
#     random.shuffle(feed.entries)
#     return feed.entries
