# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0010_auto_20161123_0657'),
        ('checker', '0011_auto_20161122_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='flag',
        ),
        migrations.AddField(
            model_name='flag',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checker.Task'),
        ),
        migrations.AddField(
            model_name='flag',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.Team'),
        ),
    ]
