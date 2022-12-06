from django.urls import path
from . import views

urlpatterns = [
    path('', views.sdttool, name='sdttool'),
    path("download/", views.downloadFile, name="downloadFile"),
    path('download/<str:hash>/', views.file_download, name="file_download"),
    # path('', views.uploadFile, name='upload'),
    # path("upload", views.uploadFile, name="uploadFile"),
]
