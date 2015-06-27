from django.db import models
from filer.fields.file import FilerFileField


class File(models.Model):
    name = models.CharField(max_length=255)
    file = FilerFileField(related_name='filer_file')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
