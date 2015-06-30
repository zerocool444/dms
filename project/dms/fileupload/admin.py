from django.contrib import admin
from .models import FilesystemEntry, File, Folder

# Register your models here.
admin.site.register(FilesystemEntry)
admin.site.register(File)
admin.site.register(Folder)
