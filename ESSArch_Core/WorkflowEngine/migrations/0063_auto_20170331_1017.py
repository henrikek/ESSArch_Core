# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-31 08:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0062_auto_20170313_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processtask',
            options={'get_latest_by': 'time_created', 'permissions': (('can_undo', 'Can undo tasks'), ('can_retry', 'Can retry tasks'))},
        ),
    ]
