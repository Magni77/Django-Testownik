# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-20 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0007_auto_20170320_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmarkmodel',
            name='test',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='testmark', to='tests.TestModel'),
        ),
    ]
