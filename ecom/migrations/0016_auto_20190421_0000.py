# Generated by Django 2.1.7 on 2019-04-21 00:00

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0015_auto_20190420_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='buyern',
            field=django_mysql.models.ListTextField(models.IntegerField(), size=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='productn',
            field=django_mysql.models.ListTextField(models.IntegerField(), size=100),
        ),
    ]
