# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_auto_20150628_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='pid',
            field=models.UUIDField(null=True),
        ),
    ]
