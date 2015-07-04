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
    owners = models.ManyToManyField(User)
    pid = models.UUIDField(null=True, blank=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def modified_by(self):
        owners = self.owners.all()
        owners_list = ""

        for owner in owners:
            owners_list += (owner.username + ",")

        return owners_list

    def type(self):
        return 'Folder'  # always a folder, right?

    def size(self):
        """
        Returns the size of the folder (i.e., its contents)
        @author Kevin Porter
        """
        descendants = self.get_descendants()
        size = 0

        for descendant in descendants:
            entry = descendant.content_object
            size += entry.size()

        return size

    def get_ptr(self):
        content_type = ContentType.objects.get(app_label='fileupload',
                                               model='folder')
        tree_ptr = FilesystemEntry.objects.get(object_id=self.id,
                                               content_type=content_type)
        return tree_ptr

    def get_children(self):
        tree_ptr = self.get_ptr()
        children = tree_ptr.get_children()
        return children

    def get_descendants(self):
        tree_ptr = self.get_ptr()
        descendants = tree_ptr.get_descendants()
        return descendants

    def items(self):
        tree_ptr = self.get_ptr()
        items = tree_ptr.get_descendant_count()
        return items

    def __str__(self):
        return self.name


class File(models.Model):
    """
    A file in the filesystem
    @author Kevin Porter
    """

    owners = models.ManyToManyField(User)
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
        content_type = ContentType.objects.get(app_label='fileupload',
                                               model='file')
        tree_ptr = FilesystemEntry.objects.get(object_id=self.id,
                                               content_type=content_type)
        return tree_ptr

    def get_descendants(self):
        tree_ptr = self.get_ptr()
        descendants = tree_ptr.get_descendants()
        return descendants

    def modified_by(self):
        owners = self.owners.all()
        owners_list = ""

        for owner in owners:
            owners_list += (owner.username + ",")

        return owners_list

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
