# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 08:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0008_auto_20160410_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='contents_count',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='follow_count',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='follower_count',
        ),
    ]