# coding: utf-8
from django.core.management.base import BaseCommand
from gorodkirov.articles.models import Article, OperationalArticle


class Command(BaseCommand):
    help = 'Импорт оперативных статей из Article в OperationalArticle.'

    def handle(self, *args, **options):
        print('Import started... ')
        operational_articles = Article.objects.filter(operatively=True).order_by('-date_created')
        for article in operational_articles:
            OperationalArticle.objects.get_or_create(article=article)
        print('Import completed! ')
