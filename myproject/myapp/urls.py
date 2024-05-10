from django.urls import path
from . import views
from .models import Task,Result

urlpatterns = [
    path('media_filelist/', views.media_filelist,name="media_filelist"),  # 定义应用程序的路径
]
