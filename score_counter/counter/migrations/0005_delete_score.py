# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 14:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0004_score'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Score',
        ),
    ]
