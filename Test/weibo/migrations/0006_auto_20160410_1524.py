# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0005_auto_20160410_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(max_length=100),
        ),
    ]