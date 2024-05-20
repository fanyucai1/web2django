from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
# Create your views here.
from .models import Task,Result

from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
import os
from django.http import JsonResponse

def filelist(request):#查看某文件夹下的所有子文件夹
    Raw_dir = settings.MEDIA_ROOT
    my_dir = []
    for root, dirs, files in os.walk(Raw_dir):
        for d in dirs:
            #my_dir.append(os.path.join(root, d))
            my_dir.append(d)
    return render(request, 'myapp/filelist.html', {'files': my_dir})

def runoob(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'myapp/runoob.html', context)