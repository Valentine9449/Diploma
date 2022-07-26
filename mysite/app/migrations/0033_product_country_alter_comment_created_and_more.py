# Generated by Django 4.0.4 on 2022-06-08 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_comment_created_alter_order_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 8, 14, 31, 1, 873795), null=True, verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 14, 31, 1, 872795), verbose_name='Додано'),
        ),
    ]
