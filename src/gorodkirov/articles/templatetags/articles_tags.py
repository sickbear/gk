# coding: utf-8
import random
import time
import math
from datetime import datetime
from django import template
from django.conf import settings
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


def parse_word(normal_word, number):
    """Определяет падеж слова в зависимости от числительного, стоящего рядом. Для calculate_article_time()."""
    result = settings.MORPH.parse(normal_word)[0]
    result = result.make_agree_with_number(number).word
    return result


@register.simple_tag()
def calculate_article_time(date):
    """Вычисляет время жизни статьи. До суток - в минутах и часах. После - в сутках."""

    result = int((datetime.now() - date).total_seconds() // 60)  # разница в минутах
    if result >= 1440:
        result = result // 60 // 24
        case = parse_word('день', result)
        return '{} {} назад'.format(result, case)
    elif result >= 60:
        result = result // 60
        case = parse_word('час', result)
        return '{} {} назад'.format(result, case)
    elif result == 0:
        return '1 мин назад'.format(result)
    return '{} мин назад'.format(result)


@register.simple_tag()
def calculate_reading_time(text):
    """Вычисляет время чтения статьи в зависимости от количества символов.

    По данным https://sfmedia.ru/calculate/readingtime/
    Динамичный темп 1000 символов за 66.0 сек.
    Нормальный темп 1000 символов за 68.2 сек.
    Комфортный темп 1000 символов за 70.6 сек.
    time = количество символов / 1000 символов * 70.6 сек / 60 сек
    """
    symbols_count = len(text)
    time = symbols_count / 1000 * 70.6 / 60  # время прочтения в минутах
    time = math.ceil(time)  # округление в большую сторону
    return 'Читать {} мин'.format(time)


