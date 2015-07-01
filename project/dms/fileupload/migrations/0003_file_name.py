# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_auto_20150701_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
