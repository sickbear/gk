# coding: utf-8
import random
from django import template
from .. import queries as articles_queries


register = template.Library()


@register.simple_tag()
def show_urgent_article():
    """Отображает статью в разде Срочно."""
    return articles_queries.get_urgent_article()


@register.simple_tag()
def show_chronicle_artciles(rubric):
    """Отображает статьи Хроники."""
    return articles_queries.get_chronicle_artciles(rubric)


@register.simple_tag()
def show_popular_tags(rubric):
    """Отображает популярные теги."""
    return articles_queries.get_popular_tags(rubric)

