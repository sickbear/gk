# Generated by Django 2.2.6 on 2019-10-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0004_auto_20191016_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo', verbose_name='Логотип')),
            ],
        ),
    ]
