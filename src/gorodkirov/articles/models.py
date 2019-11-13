# # coding=utf-8
import datetime
from django.db import models
from django.shortcuts import get_object_or_404
from tinymce import HTMLField
from mptt.models import MPTTModel, TreeForeignKey


class InformationType(models.Model):
    """Тип информации."""
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Тип информации'
        verbose_name_plural = 'Типы информации'
        db_table = 'articles_informationtype'

    def __str__(self):
        return self.name


class ArticleType(models.Model):
    """Тип статьи."""
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Шаблон отображения'
        verbose_name_plural = 'Типы шаблонов'
        db_table = 'articles_articletype'

    def __str__(self):
        return self.name


class Author(models.Model):
    """Автор статьи."""
    name = models.CharField('Имя Фамилия', max_length=255)
    photo = models.ImageField('Аватар', upload_to='authors_photos', null=True, blank=True)

    class Meta:
        verbose_name = 'Автор статьи'
        verbose_name_plural = 'Авторы статей'
        db_table = 'articles_author'

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Текстовый тег."""
    text = models.CharField('Текст', max_length=30, help_text='Максимальная длина тега - 30 символов')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        db_table = 'articles_tag'

    def __str__(self):
        return self.text


class PopularTag(models.Model):
    """Популярный тег рубрики."""
    tag = models.ForeignKey('Tag', verbose_name='Тег', related_name='tags', on_delete=models.CASCADE)
    rubric = models.ForeignKey(
        'Rubric', verbose_name='Рубрика', related_name='tags', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Популярный тег'
        verbose_name_plural = 'Популярные теги'
        ordering = ['tag__text']

    def __str__(self):
        return self.tag.text


class Rubric(MPTTModel):
    """Рубрика статьи."""
    name = models.CharField('Название', max_length=255, db_index=True)
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    slug = models.SlugField('URL', max_length=300, editable=True, db_index=True, blank=True)
    seo_title = models.CharField('Заголовок страницы', max_length=255, blank=True)
    seo_description = models.CharField('Описание', max_length=255, blank=True)
    seo_keywords = models.CharField('Ключевые слова', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        db_table = 'articles_rubric'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    """Статья."""
    AGE_CHOICES = (('0', '0'), ('6', '6+'), ('12', '12+'), ('16', '16+'), ('18', '18+'),)

    active = models.BooleanField('Активная', default=False, db_index=True)
    rubric = TreeForeignKey(Rubric, verbose_name='Рубрика', related_name='articles', on_delete=models.CASCADE)
    date_created = models.DateTimeField('Дата создания', default=datetime.datetime.now, db_index=True, editable=False)
    date_sort = models.DateTimeField('Дата сортировки', blank=True, null=True, db_index=True)
    published_at = models.DateTimeField('Начало публикации', db_index=True, blank=True, null=True)
    published_to = models.DateTimeField('Конец публикации', db_index=True, blank=True, null=True)
    info_type = models.ForeignKey(
        InformationType, verbose_name='Тип информации', related_name='articles',
        db_index=True, default=1, on_delete=models.CASCADE)
    article_type = models.ForeignKey(
        ArticleType, verbose_name='Шаблон', db_index=True, related_name='articles', on_delete=models.CASCADE)
    age_restriction = models.CharField('Возрастное ограничение', max_length=2, choices=AGE_CHOICES, default=0)
    title = models.CharField('Заголовок статьи', max_length=500, db_index=True)
    slug = models.SlugField('URL',  db_index=True, max_length=500, unique=False, default='')
    seo_title = models.CharField('Тайтл (SEO)', max_length=300, blank=True)
    seo_description = models.CharField('Описание (SEO)', max_length=300, blank=True)
    seo_keywords = models.CharField('Ключ.слова (SEO)', max_length=300, blank=True)
    author = models.ForeignKey(
        Author, verbose_name='Автор', related_name='articles', null=True, blank=True, on_delete=models.CASCADE)
    main_photo = models.ImageField('Фото', upload_to='main_photos', blank=True, null=True)
    text = HTMLField('Текст статьи')
    tags = models.ManyToManyField(Tag, verbose_name='Теги', related_name='articles', blank=True)
    urgently = models.BooleanField('Выводить в «Срочном»', default=False, db_index=True)
    operatively = models.BooleanField('Выводить в «Оператовном»', default=False, db_index=True)
    main = models.BooleanField('Выводить в «Главных новостях»', default=False, db_index=True)
    city_new = models.BooleanField('Выводить в «Городских новостях»', default=False, db_index=True)
    big_block = models.BooleanField('Выводить в «Большом блоке»', default=False, db_index=True)
    chronicle = models.BooleanField('Выводить в «Хронике»', default=False, db_index=True)
    test_drive = models.BooleanField('Выводить в «Тест-драйве»', default=False, db_index=True)
    editors_choice = models.BooleanField('Выбор редакции', default=False, db_index=True)
    for_yandex = models.BooleanField('Статья для Яндекса', db_index=True)
    for_rss = models.BooleanField('Статья для RSS', db_index=True)
    for_dzen = models.BooleanField('Статья для DZEN', db_index=True)
    twitter_export = models.BooleanField('Экспорт в Твиттер', default=False, db_index=True)
    twitter_exported = models.BooleanField(default=False, editable=False, db_index=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        get_latest_by = "date_created"
        ordering = ['-date_sort']
        permissions = (('can_preview', 'Разрешен предпросмотр статей'),)
        db_table = 'articles_article'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        # устанавливает дату сортировки
        if not self.date_sort:
            self.date_sort = datetime.datetime.now().replace(microsecond=0)

        # добавляет статью в оперативное
        if self.operatively:
            OperationalArticle.objects.get_or_create(article=self)
        elif not self.operatively and OperationalArticle.objects.filter(article=self).exists():
            OperationalArticle.objects.get(article=self).delete()
        super(Article, self).save(*args, **kwargs)

        # добавляет статью в городские подробности
        if self.city_new:
            CityDetails.objects.get_or_create(article=self)
        elif not self.city_new and CityDetails.objects.filter(article=self).exists():
            CityDetails.objects.get(article=self).delete()
        super(Article, self).save(*args, **kwargs)

        # добавляет статью в хронику
        if self.chronicle:
            ChronicleArticle.objects.get_or_create(article=self)
        elif not self.chronicle and ChronicleArticle.objects.filter(article=self).exists():
            ChronicleArticle.objects.get(article=self).delete()
        super(Article, self).save(*args, **kwargs)

        # добавляет статью в тест-драйв
        if self.test_drive:
            TestDriveArticle.objects.get_or_create(article=self)
        elif not self.test_drive and TestDriveArticle.objects.filter(article=self).exists():
            TestDriveArticle.objects.get(article=self).delete()
        super(Article, self).save(*args, **kwargs)

    def is_published(self):
        return self.active and self.published_at is not None and self.published_at <= datetime.datetime.now()
    is_published.short_description = 'Опубликовано'
    is_published.boolean = True


class OperationalArticle(models.Model):
    """Оперативная статья."""
    article = models.ForeignKey(
        Article, verbose_name='Статья', related_name='operational_articles', on_delete=models.CASCADE)
    bold = models.BooleanField('Жирный заголовок', default=False)

    class Meta:
        verbose_name = '«Оперативное»'
        verbose_name_plural = '«Оперативное»'
        db_table = 'articles_operatively'

    def __str__(self):
        return self.article.title

    def get_published_at_date(self):
        return Article.objects.filter(id=self.article.id).first().published_at
    get_published_at_date.short_description = 'Начало публикации'

    def get_published_to_date(self):
        return Article.objects.filter(id=self.article.id).first().published_to
    get_published_to_date.short_description = 'Конец публикации'


class CityDetails(models.Model):
    """Статья для блока Городские подробности."""
    BLOCK_CHOICES = (('1', '1 экран'), ('2', '2 экран'), ('3', '3 экран'),)

    article = models.ForeignKey(Article, verbose_name='Статья',  related_name='city_details', on_delete=models.CASCADE)
    placement_unit = models.CharField('Место', max_length=1, choices=BLOCK_CHOICES, default=1)

    class Meta:
        verbose_name = '«Городские новости»'
        verbose_name_plural = '«Городские новости»'
        db_table = 'articles_city_news'

    def __str__(self):
        return self.article.title

    def get_info_type(self):
        return Article.objects.filter(id=self.article.id).first().info_type
    get_info_type.short_description = 'Тип'

    def get_published_at_date(self):
        return Article.objects.filter(id=self.article.id).first().published_at
    get_published_at_date.short_description = 'Начало публ.'

    def get_published_to_date(self):
        return Article.objects.filter(id=self.article.id).first().published_to
    get_published_to_date.short_description = 'Конец публ.'


class ChronicleRubric(models.Model):
    """Рубрика хроники."""
    name = models.CharField('Название', max_length=255, db_index=True)
    slug = models.SlugField('URL', max_length=300, editable=True, db_index=True, blank=True)
    seo_title = models.CharField('Заголовок страницы', max_length=255, blank=True)
    seo_description = models.CharField('Описание', max_length=255, blank=True)
    seo_keywords = models.CharField('Ключевые слова', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Тема хроники'
        verbose_name_plural = 'Темы хроники'
        db_table = 'articles_chronicle_rubric'

    def __str__(self):
        return self.name


class ChronicleArticle(models.Model):
    """Статья хроники."""
    article = models.ForeignKey(
        Article, verbose_name='Статья',  related_name='chronicle_articles', on_delete=models.CASCADE)
    topic = models.ForeignKey(ChronicleRubric, verbose_name='Тема хроники', default=1, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '«Хроника»'
        verbose_name_plural = '«Хроника»'
        db_table = 'articles_chronicle'

    def __str__(self):
        return self.article.title


class TestDriveArticle(models.Model):
    """Статья тест-драйва."""
    article = models.ForeignKey(
        Article, verbose_name='Статья', related_name='test_drive_articles',  on_delete=models.CASCADE)
    subtitle = models.CharField('Подзаголовок статьи', max_length=500, db_index=True)

    class Meta:
        verbose_name = '«Тест-драйв»'
        verbose_name_plural = '«Тест-драйвы»'
        db_table = 'articles_test_drive'

    def __str__(self):
        return self.article.title
