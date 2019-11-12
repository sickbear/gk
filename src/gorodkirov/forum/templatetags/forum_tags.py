# coding=utf-8
# import HTMLParser

from django import template
# from obscene_words_filter import get_default_filter

from ..models import Thread
# from ..views import replace_text_with_smileys, build_smileys_table

register = template.Library()
# html_parser = HTMLParser.HTMLParser()


@register.simple_tag()
def get_last_messages(count=6):
    """ Последние сообщения на форуме """
    return (Thread.objects.exclude(article_system_id__gt=0).distinct().
            order_by('-last_updated')[:count])


@register.simple_tag()
def get_last_articles(count=6):
    """ Последние комментарии к статьям """
    return (Thread.objects.exclude(article_system_id=0).distinct()
            .order_by('-last_updated')[:count])


@register.simple_tag()
def get_threads(count=10):
    """ Все статьи """
    return Thread.objects.all().order_by('-last_updated')[:count]


# @register.filter
# def unescape(value):
#     return html_parser.unescape(value)


# @register.filter
# def replace_smileys(value):
#     return replace_text_with_smileys(value)
#
#
# @register.assignment_tag
# def smileys_table():
#     """
#     Возвращает таблицу уникальных смайлов.
#
#     {'/static/img/smile.png': ':-)', ...}
#     """
#     table = build_smileys_table()
#     unique_smiles = {}
#     for smile_key, smile_path in table.iteritems():
#         if not smile_path in unique_smiles:
#             unique_smiles[smile_path] = smile_key
#     return unique_smiles


@register.simple_tag
def empty():
    return ''


@register.simple_tag
def endthumbnail():
    return ''


# @register.filter()
# def filter_text(text):
#     return get_default_filter().mask_bad_words(text)
#     return filter.filter_text(text)