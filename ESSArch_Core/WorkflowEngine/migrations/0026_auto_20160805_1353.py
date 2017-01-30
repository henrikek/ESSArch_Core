"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch Core
    Copyright (C) 2005-2017 ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0025_remove_processstep_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='type',
            field=models.IntegerField(choices=[(0, 'Receive new object'), (5, 'The object is ready to remodel'), (9, 'New object stable'), (10, "Object don't exist in AIS"), (11, "Object don't have any projectcode in AIS"), (12, "Object don't have any local policy"), (13, 'Object already have an AIP!'), (14, 'Object is not active!'), (19, 'Object got a policy'), (20, 'Object not updated from AIS'), (21, 'Object not accepted in AIS'), (24, 'Object accepted in AIS'), (25, 'SIP validate'), (30, 'Create AIP package'), (40, 'Create package checksum'), (50, 'AIP validate'), (60, 'Try to remove IngestObject'), (1000, 'Write AIP to longterm storage'), (1500, 'Remote AIP'), (2009, 'Remove temp AIP object OK'), (3000, 'Archived'), (5000, 'ControlArea'), (5100, 'WorkArea'), (9999, 'Deleted')], null=True),
        ),
    ]