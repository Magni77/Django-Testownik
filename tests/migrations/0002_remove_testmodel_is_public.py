# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-03 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='is_public',
        ),
    ]
