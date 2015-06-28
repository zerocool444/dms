from .models import File, Folder
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('name', 'file', 'created', 'modified', 'pid', 'parent',)


class FolderSerializer(serializers.ModelSerializer):
    pid = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Folder
        fields = ('name', 'created', 'modified', 'pid', 'parent',)

'''
Not sure if this is needed. Saw the idea... somewhere.
'''
class SubfolderSerializer(serializers.ModelSerializer):
    pid = serializers.CharField(max_length=255, read_only=True)
    parent = FolderSerializer()

    class Meta:
        model = Folder
        fields = ('name', 'created', 'modified', 'pid', 'parent',)
