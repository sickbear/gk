# Generated by Django 2.2.6 on 2019-10-23 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_operationalarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationalarticle',
            name='order',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Порядок вывода'),
        ),
        migrations.AlterField(
            model_name='operationalarticle',
            name='bold',
            field=models.BooleanField(default=False, verbose_name='Жирный заголовок'),
        ),
    ]
