# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('flis_horison_scanning', '0012_auto_20170316_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeofsignal',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='typeofsignal',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]