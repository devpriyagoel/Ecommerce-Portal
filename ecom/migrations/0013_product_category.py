# Generated by Django 2.1.7 on 2019-04-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0012_auto_20190420_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('all', 'All'), ('sports', 'Sports'), ('electric', 'Electric Appliances')], default='all', max_length=50),
        ),
    ]
