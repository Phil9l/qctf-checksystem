# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 06:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0008_auto_20161122_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 23, 6, 48, 16, 38480, tzinfo=utc)),
        ),
    ]