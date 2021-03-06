# Generated by Django 2.2.6 on 2019-10-28 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20191023_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement_unit', models.CharField(choices=[('1', '1 блок'), ('2', '2 блок'), ('3', '3 блок')], default=1, max_length=1, verbose_name='Место размещения')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Новость блока «Городские новости»',
                'verbose_name_plural': 'Новости блока «Городские новости»',
                'db_table': 'articles_city_news',
            },
        ),
    ]
