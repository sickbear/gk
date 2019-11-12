# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxLengthValidator


class Category(models.Model):
    """Категория."""
    name = models.CharField('Название', max_length=200)
    user = models.ForeignKey(
        User, related_name='categories', editable=False, verbose_name='Создатель', on_delete=models.CASCADE)
    description = models.TextField('Описание', blank=True)
    sections_count = models.PositiveIntegerField('Разделов', default=0, editable=False, db_index=True)
    last_updated = models.DateTimeField('Последнее обновление', auto_now=True, db_index=True)
    seo_title = models.CharField('Заголовок (SEO)', blank=True, max_length=250)
    seo_keywords = models.CharField('Ключевые слова (SEO)', blank=True, max_length=150)
    seo_description = models.CharField('Описание (SEO)', blank=True, max_length=250)
    sort_key = models.IntegerField('Ключ сортировки', default=0, db_index=True)
    is_hidden = models.BooleanField('Закрыта', default=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum_sections', args=[str(self.id)])

    def get_seo_title(self):
        return self.seo_title or '%s - Центральный форум города Кирова' % self.name

    def get_seo_keywords(self):
        return self.seo_keywords

    def get_seo_description(self):
        return self.seo_description

    def threads_count(self):
        """ Возвращает количество тем в категории """
        return Thread.objects.filter(section__category=self).count()


class Section(models.Model):
    """Раздел категории."""
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='sections', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='sections', editable=False, verbose_name='Создатель', on_delete=models.CASCADE)
    threads_count = models.PositiveIntegerField('Тем', default=0, editable=False, db_index=True)
    last_updated = models.DateTimeField('Последнее обновление', auto_now=True, db_index=True)
    seo_title = models.CharField('Заголовок (SEO)', blank=True, max_length=250)
    seo_keywords = models.CharField('Ключевые слова (SEO)', blank=True, max_length=150)
    seo_description = models.CharField('Описание (SEO)', blank=True, max_length=250)
    sort_key = models.IntegerField('Ключ сортировки', default=0, db_index=True)
    is_hidden = models.BooleanField('Закрыта', default=False)

    class Meta:
        verbose_name = 'Раздел категории'
        verbose_name_plural = 'Разделы категории'
        ordering = ['name']

    def __str__(self):
        return '%s - %s' % (self.category, self.name)

    def get_absolute_url(self):
        return reverse('forum_threads', args=[str(self.category_id), str(self.id)])

    def get_seo_title(self):
        return (self.seo_title
                or '%s - %s' % (self.name, self.category.get_seo_title()))

    def get_seo_keywords(self):
        return self.seo_keywords or self.category.seo_keywords

    def get_seo_description(self):
        return self.seo_description or self.category.get_seo_description()


class Thread(models.Model):
    """Тема в разделe."""
    comments_allowed = models.BooleanField('Комментирование разрешено', default=True, db_index=True)
    name = models.CharField('Название', max_length=200)
    # у обычных форумных тем это поле всегда 0, иначе это статья
    article_system_id = models.IntegerField('id статьи из статейной системы', default=0, editable=False, db_index=True)
    text = models.TextField('Текст темы')
    section = models.ForeignKey(Section, verbose_name='Секция', related_name='threads', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='threads', editable=False, verbose_name='Создатель', on_delete=models.CASCADE)
    posts_count = models.PositiveIntegerField('Ответов', default=0, editable=False, db_index=True)
    date_created = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True)
    last_updated = models.DateTimeField('Дата обновления', db_index=True)
    image1 = models.ImageField('Изображение 1', upload_to='thread_images', blank=True)
    image2 = models.ImageField('Изображение 2', upload_to='thread_images', blank=True)
    image3 = models.ImageField('Изображение 3', upload_to='thread_images', blank=True)
    seo_title = models.CharField('Заголовок (SEO)', blank=True, max_length=250)
    seo_keywords = models.CharField('Ключевые слова (SEO)', blank=True, max_length=150)
    seo_description = models.CharField('Описание (SEO)', blank=True, max_length=250)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['name']

    def __str__(self):
        return '%s - %s' % (self.section, self.name)

    def get_absolute_url(self):
        return reverse('forum_thread', args=[str(self.section.category_id), str(self.section_id), str(self.id)])

    def save(self, auto_now=True, *args, **kwargs):
        if auto_now:
            self.last_updated = datetime.datetime.now()
        super(Thread, self).save(*args, **kwargs)

    def images(self):
        """Возвращает список загруженных изображений."""
        return [x for x in [
            self.image1,
            self.image2,
            self.image3
        ] if x]

    def get_seo_title(self):
        default_seo_title = '%s - %s - Центральный форум города Кирова' % (self.name, self.section.name)
        return self.seo_title or default_seo_title

    def get_seo_keywords(self):
        return self.seo_keywords or self.section.seo_keywords or self.section.category.seo_keywords

    def get_seo_description(self):
        return self.seo_description or self.section.seo_description or self.section.category.seo_description

    def author_name(self):
        """Возвращает имя автора, или имя анонимного комментатора."""
        return self.user.first_name or self.user.last_name or self.user.username


class Post(models.Model):
    """Сообщениe в теме."""
    text = models.TextField('Текст сообщения', validators=[MaxLengthValidator(1000)])
    user = models.ForeignKey(User, related_name='posts', editable=False, verbose_name='Создатель',
                             null=True, blank=True, on_delete=models.CASCADE)
    user_ip = models.GenericIPAddressField('Айпишник', blank=True, editable=False, null=True)
    thread = models.ForeignKey(
        Thread, verbose_name='Тема', related_name='posts', editable=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField('Дата отправки', auto_now_add=True, blank=True, null=True, db_index=True)
    last_updated = models.DateTimeField('Дата обновления', auto_now=True, blank=True, null=True, db_index=True)
    image1 = models.ImageField('Изображение 1', upload_to='posts_images', blank=True)
    image2 = models.ImageField('Изображение 2', upload_to='posts_images', blank=True)
    image3 = models.ImageField('Изображение 3', upload_to='posts_images', blank=True)

    posts_per_page = 20

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['date_created']

    def save(self, *args, **kwargs):
        if ',' in self.user_ip:
            bits = self.user_ip.split(',')
            for ip in bits:
                if ip != 'unknown':
                    self.user_ip = ip
                    break
        elif self.user_ip == 'unknown':
            self.user_ip = '0.0.0.0'

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.user, self.thread)

    def get_absolute_url(self):
        count = Post.objects.filter(thread=self.thread, id__lte=self.id).count()
        page = count / self.posts_per_page + 1
        return '%s?page=%s#post-%s' % (self.thread.get_absolute_url(), page, self.id)

    def images(self):
        """Возвращает список загруженных изображений."""
        return [x for x in [
            self.image1,
            self.image2,
            self.image3
        ] if x]

    def author_name(self):
        """Возвращает имя автора, или имя анонимного комментатора."""
        return self.user.username
