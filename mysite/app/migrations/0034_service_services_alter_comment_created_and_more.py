# Generated by Django 4.0.4 on 2022-06-09 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_product_country_alter_comment_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='services',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 9, 12, 54, 36, 459747), null=True, verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 54, 36, 458749), verbose_name='Додано'),
        ),
    ]
