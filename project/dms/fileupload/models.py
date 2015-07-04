from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Folder(models.Model):
    """
    A folder in the filesystem.
    @author Kevin Porter
    """
    owner = models.ManyToManyField(User)
    pid = models.UUIDField(null=True, blank=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def modified_by(self):
        return self.owner.user.username

    def type(self):
        return 'Folder'  # always a folder

    def size(self):
        """
        Returns the size of the folder (i.e., its contents)
        @author Kevin Porter
        """
        children = get_children()
        size = 0

        for child in children:
            entry = child.content_object
            size += entry.size()

        return size

    def get_ptr(self):
        tree_ptr = FilesystemEntry.objects.get(pk=self.id)
        return tree_ptr

    def get_children(self):
        tree_ptr = get_ptr()
        children = tree_ptr.get_children()
        return children

    def items(self):
        children = get_children()
        items = children.count()

        for child in children:
            child_items = child.items()
            items += child_items

        return items

    def __str__(self):
        return self.name


class File(models.Model):
    """
    A file in the filesystem
    @author Kevin Porter
    """

    owner = models.ManyToManyField(User)
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

    def items(self):
        # it might be cool to have support for listing the number of items
        # in a zip archive or something.
        pass

    def get_ptr(self):
        tree_ptr = FilesystemEntry.objects.get(pk=self.id)
        return tree_ptr

    def modified_by(self):
        user = self.owner.get(pk=self.id)
        username = user.username
        return username

    def __str__(self):
        return self.name


class FilesystemEntry(MPTTModel):
    """
    Generic MPTT tree representation of a filesystem entry.
    @author Kevin Porter
    """
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
