# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0012_auto_20161123_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='default_flag',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
