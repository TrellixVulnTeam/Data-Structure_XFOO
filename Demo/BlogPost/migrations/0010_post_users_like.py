# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-10-26 04:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogPost', '0009_auto_20181024_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='articles_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
