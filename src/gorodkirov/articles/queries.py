# coding=utf-8
import random
from .models import (
    Rubric, Article, OperationalArticle, CityDetails, ChronicleRubric, ChronicleArticle, TestDriveArticle
)
from gorodkirov.cmstemplates.models import NewSettings


def get_urgent_article():
    """Получает статью для раздела Срочно."""
    total_amount = 1
    article = Article.objects.filter(urgently=True).order_by('-date_sort')[:total_amount]
    if article is None:
        article = Article.objects.filter(active=True)
    return article


def get_main_news():
    """Получает статьи для раздела Главные новости."""
    total_amount = 5
    commercial_amount = NewSettings.objects.get(id=1).count
    commercial_articles = Article.objects.filter(
        main=True, active=True, info_type_id=2
    ).order_by('-date_sort')[:commercial_amount]

    editorial_amount = total_amount - commercial_articles.count()
    editorial_articles = Article.objects.filter(
        main=True, active=True, info_type_id=1
    ).order_by('-date_sort')[:editorial_amount]

    articles = commercial_articles.union(editorial_articles)
    articles = list(articles)
    random.shuffle(articles)
    return articles


class GetCityDetails:
    """Получает новости для блока Городские подробности."""
    def __init__(self):
        self.amount_city_details = 32
        self.editorial_amount_block_1 = 12
        self.editorial_amount_block_2 = 10
        self.editorial_amount_block_3 = 10
        self.commercial_amount_block_1 = 0
        self.commercial_amount_block_2 = 0
        self.commercial_amount_block_3 = 0
        self.total_commercial_amount_block_1 = NewSettings.objects.get(id=2).count
        self.total_commercial_amount_block_2 = NewSettings.objects.get(id=3).count
        self.total_commercial_amount_block_3 = NewSettings.objects.get(id=4).count
        self.articles_block_1 = []
        self.articles_block_2 = []
        self.articles_block_3 = []

    def get_commercial_block_1(self):
        commercial_articles = CityDetails.objects.filter(
            article__city_new=True, article__active=True, article__info_type_id=2, placement_unit=1
        ).exclude(article__big_block=True).values('article_id').order_by('-article__date_sort')[:self.total_commercial_amount_block_1]
        articles = Article.objects.filter(id__in=commercial_articles)
        self.commercial_amount_block_1 = articles.count()
        return articles

    def get_commercial_block_2(self):
        commercial_articles = CityDetails.objects.filter(
            article__city_new=True, article__active=True, article__info_type_id=2, placement_unit=2
        ).exclude(article__big_block=True).values('article_id').order_by('-article__date_sort')[:self.total_commercial_amount_block_2]
        articles = Article.objects.filter(id__in=commercial_articles)
        self.commercial_amount_block_2 = articles.count()
        return articles

    def get_commercial_block_3(self):
        commercial_articles = CityDetails.objects.filter(
            article__city_new=True, article__active=True, article__info_type_id=2, placement_unit=3
        ).exclude(article__big_block=True).values('article_id').order_by('-article__date_sort')[:self.total_commercial_amount_block_3]
        articles = Article.objects.filter(id__in=commercial_articles)
        self.commercial_amount_block_3 = articles.count()
        return articles

    def get_editorial(self):
        return Article.objects.filter(
            city_new=True, active=True, info_type_id=1
        ).exclude(big_block=True).order_by('-date_sort')[:self.amount_city_details]

    def get_editorial_block_1(self, queryset, last):
        articles = queryset[0:last]
        return articles

    def get_editorial_block_2(self, queryset, first, last):
        articles = queryset[first:last]
        return articles

    def get_editorial_block_3(self, queryset, first, last):
        articles = queryset[first:last]
        return articles

    def get_result(self):
        commercial_block_1 = self.get_commercial_block_1()  # получили коммерческие статьи для 1 экрана - 2
        commercial_block_2 = self.get_commercial_block_2()  # получили коммерческие статьи для 2 экрана - 1
        commercial_block_3 = self.get_commercial_block_3()  # получили коммерческие статьи для 3 экрана - 0

        editorial_amount_block_1 = self.editorial_amount_block_1 - self.commercial_amount_block_1  # необходимое количество редакционных статей на 1 экран
        editorial_amount_block_2 = self.editorial_amount_block_2 - self.commercial_amount_block_2  # необходимое количество редакционных статей на 2 экран
        editorial_amount_block_3 = self.editorial_amount_block_3 - self.commercial_amount_block_3  # необходимое количество редакционных статей на 3 экран

        self.amount_city_details = editorial_amount_block_1 + editorial_amount_block_2 + editorial_amount_block_3  # необходимое количество редакционных статей вообще
        editorial = self.get_editorial()  # получили полный queryset редакционных статей

        editorial_block_1 = self.get_editorial_block_1(editorial, editorial_amount_block_1)  # срез редакционных статей для 1 экрана
        editorial_block_2 = self.get_editorial_block_2(  # срез редакционных статей для 2 экрана
            editorial, editorial_amount_block_1, editorial_amount_block_1 + editorial_amount_block_2
        )
        editorial_block_3 = self.get_editorial_block_3(  # срез редакционных статей для 3 экрана
            editorial, editorial_amount_block_1 + editorial_amount_block_2, editorial_amount_block_1 + editorial_amount_block_2 + editorial_amount_block_3
        )

        # смешивание редакционных и коммерческих статей для каждого экрана по отдельности
        self.articles_block_1 = list(editorial_block_1.union(commercial_block_1))
        random.shuffle(self.articles_block_1)
        self.articles_block_2 = list(editorial_block_2.union(commercial_block_2))
        random.shuffle(self.articles_block_2)
        self.articles_block_3 = list(editorial_block_3.union(commercial_block_3))
        random.shuffle(self.articles_block_3)


def get_operational_news():
    """Получает новости для блока Оперативно."""
    total_amount = 6
    articles = OperationalArticle.objects.filter(
        article__operatively=True, article__active=True
    ).order_by('-article__date_sort')[:total_amount]
    return articles


def get_article_for_big_block_1():
    """Получает статью для большого блока 1 экрана."""
    article = CityDetails.objects.filter(article__big_block=True, placement_unit='1').first()
    if article is None:
        return Article.objects.filter(active=True).first()
    return Article.objects.get(id=article.article_id)


def get_article_for_big_block_2():
    """Получает статью для большого блока 2 экрана."""
    article = CityDetails.objects.filter(article__big_block=True, placement_unit='2').first()
    if article is None:
        return Article.objects.filter(active=True).first()
    return Article.objects.get(id=article.article_id)


def get_article_for_big_block_3():
    """Получает статью для большого блока 3 экрана."""
    article = CityDetails.objects.filter(article__big_block=True, placement_unit='3').first()
    if article is None:
        return Article.objects.filter(active=True).first()
    return Article.objects.get(id=article.article_id)


def get_chronicle_rubrics():
    """Получает рубрики хроники и возвращает в случайном порядке."""
    total_amount = 10
    chronicle_rubrics = ChronicleRubric.objects.all()[:total_amount]
    rubrics = list(chronicle_rubrics)
    random.shuffle(rubrics)
    return rubrics


def get_chronicle_artciles(rubric):
    """Получает статьи Хроники."""
    if rubric.id == 1:
        return None
    total_amount = 4
    chronicle_articles = ChronicleArticle.objects.filter(
        article__chronicle=True, article__active=True, topic=rubric
    ).values('article_id').order_by('-article__date_sort')[:total_amount]
    articles = Article.objects.filter(id__in=chronicle_articles)
    return articles


def get_test_drive():
    """Получает статью Тест-драйва."""
    article = TestDriveArticle.objects.filter(
        article__test_drive=True, article__active=True
    ).order_by('-article__date_sort').first()
    return article
