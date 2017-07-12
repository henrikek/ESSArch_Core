# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-04 14:01
from __future__ import unicode_literals

from django.db import migrations, models

import django.db.models.deletion

import uuid


def forwards_func(apps, schema_editor):
    RobotQueue = apps.get_model("storage", "RobotQueue")
    StorageMedium = apps.get_model("storage", "StorageMedium")
    TapeDrive = apps.get_model("storage", "TapeDrive")
    db_alias = schema_editor.connection.alias

    RobotQueue.objects.using(db_alias).all().delete()
    StorageMedium.objects.using(db_alias).all().delete()
    TapeDrive.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0017_robotqueue_tape_drive'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
        migrations.AddField(
            model_name='tapedrive',
            name='drive_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='robotqueue',
            name='tape_drive',
        ),
        migrations.RemoveField(
            model_name='storagemedium',
            name='tape_drive',
        ),
        migrations.RemoveField(
            model_name='tapedrive',
            name='id',
        ),
        migrations.AddField(
            model_name='tapedrive',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='storagemedium',
            name='tape_drive',
            field=models.OneToOneField(db_constraint=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='storage_medium', to='storage.TapeDrive'),
        ),
        migrations.AddField(
            model_name='robotqueue',
            name='tape_drive',
            field=models.ForeignKey(db_constraint=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storage.TapeDrive')
        ),
    ]