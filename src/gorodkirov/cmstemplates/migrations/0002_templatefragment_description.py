# Generated by Django 2.2.6 on 2019-10-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatefragment',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание шаблона'),
        ),
    ]
