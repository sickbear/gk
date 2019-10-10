# # coding=utf-8
# from mptt.models import MPTTModel, TreeForeignKey
#
#
# class Rubric(MPTTModel):
#     """ Рубрика статьи """
#     name = models.CharField(u'Название', max_length=255, db_index=True)
#     parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
#     slug = models.SlugField(u'URL', max_length=300, editable=True, db_index=True, blank=True)
#
#     seo_keywords = models.CharField(u'Ключевые слова', max_length=255, blank=True)
#     seo_title = models.CharField(u'Заголовок страницы', max_length=255, blank=True)
#     seo_description = models.CharField(u'Описание', max_length=255, blank=True)
#
#     class Meta:
#         verbose_name = u'Рубрика'
#         verbose_name_plural = u'Рубрики'
#         db_table = 'articles_rubric'
#
#     class MPTTMeta:
#         order_insertion_by = ['name']
#
#
# class Article(models.Model):
#     """ Статья """
#     AGE_CHOICES = (
#         ('0', '0'),
#         ('6', '6+'),
#         ('12', '12+'),
#         ('16', '16+'),
#         ('18', '18+'),
#     )
#     active = models.BooleanField(u'Активная', default=False, db_index=True)
#     urgently = models.BooleanField(u'Выводить в «Срочном»', default=False, db_index=True)
#     operatively = models.BooleanField(u'Выводить в «Оператовном»', default=False, db_index=True)
#     main = models.BooleanField(u'Выводить в «Главных новостях»', default=False, db_index=True)
#     city_news = models.BooleanField(u'Выводить в «Городских новостях»', default=False, db_index=True)
#     chronicle = models.BooleanField(u'Выводить в «»', default=False, db_index=True)
#
#     show_in_current_news = models.BooleanField(u'Отображать в блоке «Оперативно»', default=False, db_index=True)
#     dont_send = models.BooleanField(u'Не отправлять в приложение', db_index=True)
#     on_main = models.BooleanField(u'Статья на главную', db_index=True)
#     for_yandex = models.BooleanField(u'Статья для Яндекса', db_index=True)
#     for_rss = models.BooleanField(u'Статья для RSS', db_index=True)
#     for_dzen = models.BooleanField(u'Статья для DZEN', db_index=True)
#     commerce = models.BooleanField(u'Коммерческая статья', db_index=True)
#     banner_after_article = models.BooleanField(u'Баннер после статьи', db_index=True)
#
#     allow_comments = models.BooleanField(u'Разрешить комментирование', default=True)
#     rubric = TreeForeignKey(Rubric, verbose_name=u'Рубрика', related_name='articles')
#     date_created = models.DateTimeField(
#         u'Дата создания', default=datetime.datetime.now, db_index=True, editable=False)
#     date_sort = models.DateTimeField(
#         u'Дата для сортировки',
#         blank=True,
#         null=True,
#         help_text=u'Если поле пустое, проставляется при сохранении.',
#         db_index=True,
#     )
#     published_at = models.DateTimeField(u'Дата публикации', db_index=True, blank=True, null=True)
#     info_type = models.ForeignKey(
#         InformationType,
#         verbose_name=u'Тип информации',
#         related_name='articles',
#     )
#     age_restriction = models.CharField(
#         u'Возрастное ограничение', max_length=2, choices=AGE_CHOICES, default=0)
#     title = models.CharField(u'Заголовок статьи', max_length=500, db_index=True)
#     author = models.ForeignKey(
#         Author, verbose_name=u'Автор', related_name='articles', null=True, blank=True)
#     teaser = models.CharField(u'Тизер', max_length=1000, blank=True)
#     teaser2 = models.ImageField(
#         u'Новый тизер',
#         max_length=1000,
#         upload_to='article_thumbs',
#         blank=True,
#         null=True,
#     )
#     main_photo = models.ImageField(
#         u'Основная фотография', upload_to='main_photos', blank=True, null=True)
#     annotation = models.TextField(u'Аннотация', blank=True)
#     text = RedactorField(u'Текст статьи')
#
#     mp3 = models.FileField(u'MP3-файл', upload_to='mp3', blank=True)
#
#     supermarket_firm_id = models.IntegerField(u'ID фирмы на супермаркете', default=0)
#
#     twitter_export = models.BooleanField(u'Экспорт в Твиттер', default=False, db_index=True)
#     twitter_exported = models.BooleanField(default=False, editable=False, db_index=True)
#
#     place_promo = models.BooleanField(u'Отображать в Промо', db_index=True)
#     place_left_col = models.BooleanField(u'Отображать в левой колонке', db_index=True)
#     place_right_col = models.BooleanField(u'Отображать в правой колонке', db_index=True)
#     place_details = models.BooleanField(u'Отображать в Городских подробностях', db_index=True)
#
#     seo_title = models.CharField(u'Тайтл (SEO)', max_length=300, blank=True)
#     seo_description = models.CharField(u'Описание (SEO)', max_length=300, blank=True)
#     seo_keywords = models.CharField(u'Ключевые слова (SEO)', max_length=300, blank=True)
#
#     left_column = models.TextField(u'Левая колонка', blank=True)
#     right_column = models.TextField(u'Правая колонка', blank=True)
#
#     raw_tags = models.TextField(
#         u'Теги', blank=True, help_text=u'Через запятую все теги будут приведены в нижний регистр', editable=False)
#     images_count = models.IntegerField(
#         u'Количество картинок', editable=False, default=0)
#     slug = models.CharField(
#         u'Заголовок-ссылка',
#         max_length=300,
#         help_text=u'Будет сгенерирована автоматически',
#         editable=True,
#         db_index=True,
#         blank=True,
#     )
#     tags = models.ManyToManyField(
#         Tag, verbose_name=u'Теги', related_name=u'articles', blank=True)
#
#     objects = managers.ArticleManager()
#
#     class Meta:
#         verbose_name = u'Статья'
#         verbose_name_plural = u'Статьи'
#         get_latest_by = "date_created"
#         ordering = ['-date_sort']
#         permissions = (('can_preview', u'Разрешен предпросмотр статей'),)
#         db_table = 'articles_article'
#
#     def __unicode__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         """ Устанавливает дату сортировки """
#         if not self.date_sort:
#             self.date_sort = datetime.datetime.now().replace(microsecond=0)
#
#         if not self.slug:
#             self.slug = '%s-%s' % (slugify(self.title.lower()),
#                                    datetime.datetime.strftime(self.date_created or self.date_sort,
#                                                               '%Y%m%d-%H%M'))
#
#         # количество тегов img
#         document = html.fromstring(self.text)
#         self.images_count = int(document.xpath("count(//img)"))
#
#         super(Article, self).save(*args, **kwargs)