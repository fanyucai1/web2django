from django.urls import path
from . import views
from .models import Task,Result
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('filelist/', views.filelist,name="filelist"),  # 定义应用程序的路径
    path('runoob/', views.runoob),
]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
