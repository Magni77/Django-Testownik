# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-06 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_auto_20170306_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningsession',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learningsession',
            name='ended',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='learningsession',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]