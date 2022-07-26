# Generated by Django 4.0.4 on 2022-06-04 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_order_options_remove_order_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('user', 'created'), 'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 20, 59, 6, 613817), verbose_name='Додано'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 4, 20, 59, 6, 613817), null=True, verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 20, 59, 6, 612816), verbose_name='Додано'),
        ),
    ]
