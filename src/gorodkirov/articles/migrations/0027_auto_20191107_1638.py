# Generated by Django 2.2.6 on 2019-11-07 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_article_editors_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chroniclearticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chronicle_article', to='articles.Article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='citydetails',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_details', to='articles.Article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='operationalarticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operational_articles', to='articles.Article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='testdrivearticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_drive_articles', to='articles.Article', verbose_name='Статья'),
        ),
    ]
