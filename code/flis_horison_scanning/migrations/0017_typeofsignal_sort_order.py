# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('flis_horison_scanning', '0016_remove_typeofsignal_sort_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofsignal',
            name='sort_order',
            field=models.IntegerField(default=0),
        ),
    ]