# Generated by Django 4.0.4 on 2022-06-03 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_comment_created_alter_service_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(blank=True, default='Friday 03 June 2022', verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 17, 40, 16, 282160), verbose_name='Додано'),
        ),
    ]
