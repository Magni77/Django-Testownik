# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-20 08:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSettingsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buffer', models.IntegerField()),
                ('replies', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='testmodel',
            name='mark',
            field=models.ManyToManyField(blank=True, related_name='testmark', to=settings.AUTH_USER_MODEL),
        ),
    ]