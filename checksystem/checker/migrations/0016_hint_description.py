# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0015_task_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='hint',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
