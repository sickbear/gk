# Generated by Django 2.2.6 on 2019-10-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_citydetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydetails',
            name='big_block',
            field=models.BooleanField(default=False, verbose_name='Большой блок'),
        ),
        migrations.AlterField(
            model_name='citydetails',
            name='placement_unit',
            field=models.CharField(choices=[('1', '1 экран'), ('2', '2 экран'), ('3', '3 экран')], default=1, max_length=1, verbose_name='Место размещения'),
        ),
    ]
