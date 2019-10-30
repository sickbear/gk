# Generated by Django 2.2.6 on 2019-10-30 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20191030_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chroniclerubric',
            options={'verbose_name': 'Тема хроники', 'verbose_name_plural': 'Темы хроники'},
        ),
        migrations.AddField(
            model_name='chroniclerubric',
            name='name',
            field=models.CharField(db_index=True, default=1, max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chroniclerubric',
            name='seo_description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='chroniclerubric',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='chroniclerubric',
            name='seo_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='chroniclerubric',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, verbose_name='URL'),
        ),
        migrations.AlterModelTable(
            name='chroniclerubric',
            table='articles_chronicle_rubric',
        ),
        migrations.CreateModel(
            name='ChronicleArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='Статья')),
                ('topic', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.ChronicleRubric', verbose_name='Тема хроники')),
            ],
            options={
                'verbose_name': 'Новость блока «Хроника»',
                'verbose_name_plural': 'Новости блока «Хроника»',
                'db_table': 'articles_chronicle',
            },
        ),
    ]
