from .models import FilesystemEntry, File, Folder
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    pid = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = File
        fields = ('id', 'name', 'file', 'created', 'modified', 'pid', 'size', 'type',
                  'modified_by', 'items',)


class FolderSerializer(serializers.ModelSerializer):
    pid = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Folder
        fields = ('id', 'name', 'created', 'modified', 'pid', 'modified_by',
                  'items', 'type', 'size',)


class RelatedFilesystemField(serializers.RelatedField):
    '''
    @author Kevin Porter
    '''
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        '''
        @author Kevin Porter
        '''

        if isinstance(value, File):
            serializer = FileSerializer(value)
        elif isinstance(value, Folder):
            serializer = FolderSerializer(value)
        elif isinstance(value, FilesystemEntry):
            return None
        else:
            raise Exception('Not a valid filesystem object.')

        return serializer.data


class FilesystemEntrySerializer(serializers.ModelSerializer):
    content_object = RelatedFilesystemField(
        queryset=FilesystemEntry.objects.all(), required=False
        )

    class Meta:
        model = FilesystemEntry
        fields = ('id', 'content_type', 'content_object', 'object_id', 'parent',)
