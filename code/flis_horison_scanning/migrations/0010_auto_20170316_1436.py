# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('flis_horison_scanning', '0009_typeofasignal'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TypeOfASignal',
            new_name='TypeOfSignal',
        ),
    ]