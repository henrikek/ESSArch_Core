# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups_manager', '0003_0_5_0_rename_reverse_relations_with_vars'),
        ('ess.auth', '0005_notification_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='current_organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups_manager.Group'),
        ),
    ]