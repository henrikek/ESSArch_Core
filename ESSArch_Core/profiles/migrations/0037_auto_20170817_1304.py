# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-17 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0036_auto_20170817_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profileipdata',
            options={'ordering': ['version']},
        ),
    ]
