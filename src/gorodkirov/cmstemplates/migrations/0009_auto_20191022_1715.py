# Generated by Django 2.2.6 on 2019-10-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0008_auto_20191022_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsettings',
            name='commercial_main_news',
            field=models.PositiveSmallIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], verbose_name='Количество коммерч. статей'),
        ),
    ]
