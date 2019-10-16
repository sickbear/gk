# Generated by Django 2.2.6 on 2019-10-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25, verbose_name='Название шаблона')),
                ('text', models.TextField(blank=True, default='', verbose_name='Текст шаблона')),
            ],
            options={
                'verbose_name': 'Файл шаблона',
                'verbose_name_plural': 'Файлы шаблона',
            },
        ),
    ]
