# Generated by Django 4.0.4 on 2022-06-03 11:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0017_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 14, 27, 7, 508160), verbose_name='Додано'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=500, verbose_name='Коментарій')),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 6, 3, 14, 27, 7, 508160), verbose_name='Добавлен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Коментарій',
                'verbose_name_plural': 'Коментарії',
                'ordering': ('user', 'created'),
            },
        ),
    ]
