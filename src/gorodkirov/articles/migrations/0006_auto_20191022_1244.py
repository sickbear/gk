# Generated by Django 2.2.6 on 2019-10-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20191022_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', max_length=500, verbose_name='URL'),
        ),
    ]
