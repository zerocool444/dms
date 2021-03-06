from django.conf.urls import include, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


file = [
    url(r'^$', views.FileList.as_view(), name='list_create'),
    url(r'^(?P<pk>[0-9]+)/$', views.FileDetail.as_view(), name='detail'),
    url(r'^(?P<file_id>\d+)/', views.download, name="download"),
    url(r'^upload/$', views.UploadFile.as_view(), name='upload'),
]

folder = [
    url(r'^$', views.FolderList.as_view(), name='list_create'),
    url(r'^(?P<pk>[0-9]+)/$', views.FolderDetail.as_view(), name='detail'),
]

filesystem = [
    url(r'^file/', include(file, namespace='file')),
    url(r'^folder/', include(folder, namespace='folder')),
    url(r'^$', views.FilesystemEntryList.as_view(), name='list_create'),
    url(r'^(?P<pk>[0-9]+)/$', views.FilesystemEntryDetail.as_view(), name='detail'),

]

urlpatterns = [
    url(r'^api/filesystem/', include(filesystem, namespace='api')),
    url(r'^$', views.index, name="index"),
    url(r'^browser/$', views.browser, name='browser'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
