# Generated by Django 2.2.6 on 2019-10-30 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20191030_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestDriveArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(db_index=True, max_length=500, verbose_name='Подзаголовок статьи')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Новость блока «Тест-драйв»',
                'verbose_name_plural': 'Новости блока «Тест-драйв»',
                'db_table': 'articles_test_drive',
            },
        ),
    ]
