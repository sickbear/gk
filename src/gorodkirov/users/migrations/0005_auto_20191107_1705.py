# Generated by Django 2.2.6 on 2019-11-07 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Телефон'),
        ),
    ]
