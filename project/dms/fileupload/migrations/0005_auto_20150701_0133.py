# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0004_auto_20150701_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='updated',
            new_name='modified',
        ),
    ]
