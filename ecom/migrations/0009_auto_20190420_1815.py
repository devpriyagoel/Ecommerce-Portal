# Generated by Django 2.1.7 on 2019-04-20 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_auto_20190420_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='cart',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecom.Cart'),
            preserve_default=False,
        ),
    ]
