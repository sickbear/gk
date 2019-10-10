# coding: utf-8

from __future__ import print_function, unicode_literals
import feedparser
import random
from django import template

from .. import models as m
from .. import queries as q


register = template.Library()


@register.assignment_tag()
def get_rubrics():
    news_rubric = m.Rubric.objects.get(name=u'Новости')
    return news_rubric.get_descendants().select_related('articles').all()


@register.assignment_tag()
def get_articles_in_header(count=1):
    return q.get_articles_in_header(count=count)



@register.assignment_tag()
def get_popular_tags():
    return m.PopularTag.objects.filter(rubric__isnull=True)



@register.assignment_tag()
def get_popular_tags_for_rubric(rubric):
    return m.PopularTag.objects.filter(rubric=rubric)


@register.assignment_tag()
def get_medianethrics_entry():
    feed = feedparser.parse('https://mediametrics.ru/partner/inject/online.ru.rss')
    random.shuffle(feed.entries)
    return feed.entries
