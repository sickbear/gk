# Generated by Django 2.2.6 on 2019-10-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20191023_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Начало публикации'),
        ),
    ]