# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-09 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20170409_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learningsession',
            name='wrong_answers',
        ),
    ]
