# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='encoding',
        ),
        migrations.RemoveField(
            model_name='file',
            name='filename',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default='', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='pid',
            field=models.UUIDField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='folder',
            name='pid',
            field=models.UUIDField(null=True, blank=True),
        ),
    ]
