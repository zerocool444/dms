# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0005_auto_20150701_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 1, 2, 24, 55, 144997, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 1, 2, 24, 59, 888220, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
