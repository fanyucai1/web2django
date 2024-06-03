from datetime import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
import re
# Create your models here.
def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.project, filename)

class Task(models.Model):
    project= models.CharField(max_length=100, verbose_name='项目名称',primary_key=True)#primary_key主建
    author= models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name='用户名')
    creat_date=models.DateTimeField(default=datetime.now(),verbose_name="创建时间")
    fastq_R1= models.FileField(upload_to=user_directory_path,verbose_name="R1 fastq")
    fastq_R2= models.FileField(upload_to=user_directory_path,verbose_name="R2 fastq",blank=True)

    class Meta:
        verbose_name = "1.数据分析"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.project


class Result(models.Model):
    project = models.CharField(max_length=100, verbose_name='项目名称', primary_key=True)  # primary_key主建
    creat_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    log_file=models.FileField(upload_to=user_directory_path,verbose_name="log文件")
    update_time=models.DateTimeField(auto_now=True,verbose_name="结束时间")

    type_choices = (
        (0, '分析成功'),
        (1, '分析失败'),
    )
    status=models.CharField(max_length=10,choices=type_choices)
    def status_data(self):
        if self.status=="0":
            color_code="green"
            self.status="成功"
        else:
            color_code = "red"
            self.status="失败"
    class Meta:
        verbose_name = "2.分析结果"
        verbose_name_plural = verbose_name