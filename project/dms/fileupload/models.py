from django.db import models
from filer.fields.file import FilerFileField
from mptt.models import MPTTModel, TreeForeignKey

'''
class File(models.Model):
    name = models.CharField(max_length=255)
    file = FilerFileField(related_name='filer_file')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
'''


class Folder(MPTTModel):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pid = models.UUIDField(null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)

    def __str__(self):
        return self.name


class File(MPTTModel):
    name = models.CharField(max_length=255)
    file = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pid = models.UUIDField(null=True, blank=True)
    parent = TreeForeignKey(Folder, null=True, blank=True,
                            related_name='file_parent', db_index=True)

    def __str__(self):
        return self.name
