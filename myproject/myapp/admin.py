from datetime import datetime

from django.contrib import admin,messages
from django.utils.html import format_html

from .models import Task,Result
from .forms import TaskForm,ResultForm
import os,subprocess
from django.conf import settings
from django.db import transaction
from django.utils import timezone

admin.site.site_header = '微生物数据分析系统'
admin.site.site_title="123"
admin.site.index_title ="App列表:"

class TaskAdmin(admin.ModelAdmin):
    form=TaskForm
    #信息开始上传时候显示
    fieldsets = [
        (None, {"fields": ["project"]}),
        ('文件上传', {"fields": ["fastq_R1","fastq_R2"]}),
    ]
    #信息上传完新增页面展示的内容
    list_display = ('project','author','creat_date','fastq_R1','fastq_R2')
    #list_editable = ('fastq_R1','fastq_R2')  # 哪些元素可修改
    #list_per_page = 5 #每页展示多少条记录
    def save_model(self, request, obj, form, change):
        with transaction.atomic():
            ################################记录提交任务的用户，并分别验证fastq文件的完整性
            obj.author = request.user
            obj.save()
            ##########################
            R1 = os.path.join(settings.MEDIA_ROOT, str(obj.fastq_R1))
            cmd=""
            if obj.fastq_R2:
                R2 = os.path.join(settings.MEDIA_ROOT, str(obj.fastq_R2))
                cmd = f"java -jar /Users/yfan/Desktop/git/web2django/myproject/software/validatefastq-assembly-0.1.1.jar -i {R1} -j {R2}"
            else:
                cmd = f"java -jar /Users/yfan/Desktop/git/web2django/myproject/software/validatefastq-assembly-0.1.1.jar -i {R1}"
            try:
                subprocess.check_call(cmd,shell=True)
            except subprocess.CalledProcessError as e:
                messages.error(request, "上传文件格式不正确，请重新上传！")#
                dir=os.path.dirname(R1)
                if obj.fastq_R1:
                    obj.fastq_R1.delete(save=False)
                if obj.fastq_R2:
                    obj.fastq_R2.delete(save=False)
                transaction.set_rollback(True)
                os.rmdir(dir)#删除文件上传文件夹


class ResultAdmin(admin.ModelAdmin):
    form=ResultForm
    list_display = ('project', 'creat_date','update_time')
    def has_add_permission(self, request):#在页面上禁止添加
        return False
    def has_change_permission(self, request):#在页面上禁止修改
        return False
    def has_delete_permission(self, request):  #在页面上禁止删除
        return False


admin.site.register(Task,TaskAdmin)
admin.site.register(Result,ResultAdmin)