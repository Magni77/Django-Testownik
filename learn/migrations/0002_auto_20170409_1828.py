# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-09 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionstatistic',
            name='attempts',
        ),
        migrations.AddField(
            model_name='questionstatistic',
            name='correct_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionstatistic',
            name='wrong_answers',
            field=models.IntegerField(default=0),
        ),
    ]