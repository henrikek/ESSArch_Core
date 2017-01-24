# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-18 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0033_auto_20160818_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eventIdentifierValue',
        ),
        migrations.AlterField(
            model_name='event',
            name='eventDateTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]