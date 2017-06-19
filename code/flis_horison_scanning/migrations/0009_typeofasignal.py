# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('flis_horison_scanning', '0008_auto_20170316_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfASignal',
            fields=[
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]