from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Folder(models.Model):
    pid = models.UUIDField(null=True, blank=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class File(models.Model):
    pid = models.UUIDField(null=True, blank=True)
    name = models.CharField(max_length=255)
    file = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def type(self):
        name = self.file.name
        extension = name.split('.')[-1]
        return extension

    def size(self):
        return self.file.size

    def __str__(self):
        return self.name


class FilesystemEntry(MPTTModel):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children')

    def __str__(self):
        entry_type = ContentType.objects.get(app_label='fileupload',
                                             model=self.content_type)
        entry = entry_type.get_object_for_this_type(pk=self.object_id)
        return entry.__str__()
