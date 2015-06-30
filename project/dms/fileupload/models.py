from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class FilesystemEntry(MPTTModel):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = TreeForeignKey('self', null=True, blank=True,
        related_name='children')


class Folder(models.Model):
    pid = models.UUIDField(null=True, blank=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class File(models.Model):
    pid = models.UUIDField(null=True, blank=True)
    file = models.FileField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name
