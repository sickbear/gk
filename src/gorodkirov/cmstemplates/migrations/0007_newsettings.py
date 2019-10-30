# Generated by Django 2.2.6 on 2019-10-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0006_auto_20191021_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commercial_main_news', models.PositiveSmallIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Количество коммерческих статей в Главном')),
            ],
            options={
                'verbose_name': 'Настройки новостей',
                'verbose_name_plural': 'Настройки новостей',
            },
        ),
    ]
