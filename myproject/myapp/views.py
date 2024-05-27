from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
# Create your views here.
from .models import Task,Result

from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
import os
from django.http import JsonResponse
from .forms import TaskForm
def add_Task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()
    return render(request, 'change_form.html', {'form': form})