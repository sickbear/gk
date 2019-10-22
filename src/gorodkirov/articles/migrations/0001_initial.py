# Generated by Django 2.2.6 on 2019-10-21 14:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя Фамилия')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='authors_photos', verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'Автор статьи',
                'verbose_name_plural': 'Авторы статей',
                'db_table': 'articles_author',
            },
        ),
        migrations.CreateModel(
            name='InformationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип статьи',
                'verbose_name_plural': 'Типы статей',
                'db_table': 'articles_informationtype',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Максимальная длина тега - 30 символов', max_length=30, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'db_table': 'articles_tag',
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=300, verbose_name='URL')),
                ('seo_title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок страницы')),
                ('seo_description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('seo_keywords', models.CharField(blank=True, max_length=255, verbose_name='Ключевые слова')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='articles.Rubric')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'db_table': 'articles_rubric',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(db_index=True, default=False, verbose_name='Активная')),
                ('date_created', models.DateTimeField(db_index=True, default=datetime.datetime.now, editable=False, verbose_name='Дата создания')),
                ('date_sort', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата для сортировки')),
                ('published_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата публикации')),
                ('age_restriction', models.CharField(choices=[('0', '0'), ('6', '6+'), ('12', '12+'), ('16', '16+'), ('18', '18+')], default=0, max_length=2, verbose_name='Возрастное ограничение')),
                ('title', models.CharField(db_index=True, max_length=500, verbose_name='Заголовок статьи')),
                ('slug', models.SlugField(default='', max_length=500, unique=True, verbose_name='URL')),
                ('seo_title', models.CharField(blank=True, max_length=300, verbose_name='Тайтл (SEO)')),
                ('seo_description', models.CharField(blank=True, max_length=300, verbose_name='Описание (SEO)')),
                ('seo_keywords', models.CharField(blank=True, max_length=300, verbose_name='Ключевые слова (SEO)')),
                ('main_photo', models.ImageField(blank=True, null=True, upload_to='main_photos', verbose_name='Основная фотография')),
                ('text', tinymce.models.HTMLField(verbose_name='Текст статьи')),
                ('urgently', models.BooleanField(db_index=True, default=False, verbose_name='Выводить в «Срочном»')),
                ('operatively', models.BooleanField(db_index=True, default=False, verbose_name='Выводить в «Оператовном»')),
                ('main', models.BooleanField(db_index=True, default=False, verbose_name='Выводить в «Главных новостях»')),
                ('city_new', models.BooleanField(db_index=True, default=False, verbose_name='Выводить в «Городских новостях»')),
                ('chronicle', models.BooleanField(db_index=True, default=False, verbose_name='Выводить в «Хронике»')),
                ('test_drive', models.BooleanField(db_index=True, default=False, verbose_name='Выводить в «Тест-драйве»')),
                ('for_yandex', models.BooleanField(db_index=True, verbose_name='Статья для Яндекса')),
                ('for_rss', models.BooleanField(db_index=True, verbose_name='Статья для RSS')),
                ('for_dzen', models.BooleanField(db_index=True, verbose_name='Статья для DZEN')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.Author', verbose_name='Автор')),
                ('info_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.InformationType', verbose_name='Тип статьи')),
                ('rubric', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.Rubric', verbose_name='Рубрика')),
                ('tags', models.ManyToManyField(blank=True, related_name='articles', to='articles.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'articles_article',
                'ordering': ['-date_sort'],
                'permissions': (('can_preview', 'Разрешен предпросмотр статей'),),
                'get_latest_by': 'date_created',
            },
        ),
    ]
