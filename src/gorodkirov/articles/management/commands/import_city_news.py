# coding: utf-8
from django.core.management.base import BaseCommand
from gorodkirov.articles.models import Article, CityDetails


class Command(BaseCommand):
    help = 'Импорт городских новостей из Article в CityDetails.'

    def handle(self, *args, **options):
        print('Import started... ')
        city_details = Article.objects.filter(city_new=True).order_by('-date_created')
        for article in city_details:
            CityDetails.objects.get_or_create(article=article)
        print('Import completed! ')
