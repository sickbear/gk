# Generated by Django 2.2.6 on 2019-11-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_populartag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='editors_choice',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Выбор редакции'),
        ),
    ]
