# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 07:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contents_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follow_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follower_count',
        ),
        migrations.RemoveField(
            model_name='userprofiles',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='contents_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='follow_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='follower_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='user',
            field=models.OneToOneField(default=datetime.datetime(2016, 4, 10, 7, 1, 52, 4000, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='weibo.User'),
            preserve_default=False,
        ),
    ]