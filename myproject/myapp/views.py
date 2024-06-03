from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
# Create your views here.
from .models import Task,Result

from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
import os,re
from django.http import JsonResponse
from .forms import TaskForm
