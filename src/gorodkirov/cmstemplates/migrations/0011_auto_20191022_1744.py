# Generated by Django 2.2.6 on 2019-10-22 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0010_auto_20191022_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsettings',
            old_name='commercial_main_news',
            new_name='count',
        ),
    ]