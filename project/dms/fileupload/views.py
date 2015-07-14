from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, filters
from .models import File, Folder, FilesystemEntry
from .serializers import (FilesystemEntrySerializer, FileSerializer,
                     FolderSerializer)


# remember to fix this later
@csrf_exempt
def index(request):
    return render(request, "fileupload/index.html")

@csrf_exempt  # remember to fix this later
def add(request):
    return render(request, "fileupload/add.html")

# remember to fix this later
@csrf_exempt
def browser(request):
    return render(request, 'fileupload/browser.html')

def download(request, file_id=0,file_link=None):
    file = get_object_or_404(File, pk=file_id)
    filename = file.file.name.split('/')[-1].replace(' ', '_')
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
    

class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FolderList(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class FolderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class FilesystemEntryList(generics.ListCreateAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('parent',)
    serializer_class = FilesystemEntrySerializer

    def get_queryset(self):
        """
        Intercepts the querystring so that checking for no parent actually
        works.
        @author Kevin Porter
        """
        queryset = FilesystemEntry.objects.all()
        parent = self.request.query_params.get('parent', None)

        if parent is not None:
            if parent == '':
                parent = None
            queryset = queryset.filter(parent=parent)

        return queryset


class FilesystemEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FilesystemEntry.objects.all()
    serializer_class = FilesystemEntrySerializer
