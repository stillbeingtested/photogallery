# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20161222_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
