# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0003_auto_20150628_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='pid',
            field=models.UUIDField(null=True, blank=True),
        ),
    ]
