from .models import FilesystemEntry, File, Folder
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    pid = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = File
        fields = ('name', 'file', 'created', 'modified', 'pid',)


class FolderSerializer(serializers.ModelSerializer):
    pid = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Folder
        fields = ('name', 'created', 'modified', 'pid',)


class RelatedFilesystemField(serializers.RelatedField):
    '''
    Jesus fucking Christ.
    @author Kevin Porter
    '''
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        '''
        For some completely fucknut reason, if I don't try to access one of the
        model properties, the whole serializer shits itself.

        Like. WTF.

        @author Kevin Porter
        '''
        value.pid
        if isinstance(value, File):
            serializer = FileSerializer(value)
        elif isinstance(value, Folder):
            serializer = FolderSerializer(value)
        else:
            raise Exception('Not a valid filesystem object.')

        return serializer.data


class FilesystemEntrySerializer(serializers.ModelSerializer):
    content_object = RelatedFilesystemField(
        queryset=FilesystemEntry.objects.all()
        )

    class Meta:
        model = FilesystemEntry
        fields = ('content_type', 'content_object', 'object_id', 'parent',)
