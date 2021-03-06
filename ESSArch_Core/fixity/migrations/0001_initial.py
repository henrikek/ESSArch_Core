# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ip', '0057_auto_20171115_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=255)),
                ('validator', models.CharField(max_length=255)),
                ('time_started', models.DateTimeField(null=True)),
                ('time_done', models.DateTimeField(null=True)),
                ('passed', models.NullBooleanField()),
                ('message', models.CharField(blank=True, max_length=255)),
                ('information_package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ip.InformationPackage')),
            ],
        ),
    ]
