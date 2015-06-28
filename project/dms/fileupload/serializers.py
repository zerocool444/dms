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
