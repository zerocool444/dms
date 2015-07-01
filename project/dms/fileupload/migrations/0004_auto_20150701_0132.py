# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0003_file_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='date_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='date_updated',
            new_name='updated',
        ),
    ]
