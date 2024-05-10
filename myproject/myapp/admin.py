from django.contrib import admin,messages
from django.db.models.signals import post_save
from django.dispatch import receiver
# Register your models here.
from .models import Task,Result
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.template.response import TemplateResponse

admin.site.site_header = '微生物数据分析系统'
admin.site.site_title="123"
admin.site.index_title ="App列表:"

class TaskAdmin(admin.ModelAdmin):
    #信息开始上传时候显示
    fieldsets = [
        (None, {"fields": ["project"]}),
        ('文件上传', {"fields": ["fastq_R1","fastq_R2"]}),
    ]
    #信息上传完新增页面展示的内容
    list_display = ('project','author','creat_date','fastq_R1','fastq_R2')
    #list_editable = ('fastq_R1','fastq_R2')  # 哪些元素可修改
    #list_per_page = 5 #每页展示多少条记录
    def save_model(self, request, obj, form, change):#默认是当前用户名
        obj.author = request.user
        obj.save()

    change_form_template = 'admin/custom_change_form.html'  # 自定义模板

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        return super().change_view(
            request,
            object_id,
            form_url,
            extra_context=extra_context,
        )

class ResultAdmin(admin.ModelAdmin):
    list_display = ('project', 'creat_date','update_time','log_file')
    def has_add_permission(self, request):#在页面上禁止添加
        return False
    def has_change_permission(self, request):#在页面上禁止修改
        return False
    def has_delete_permission(self, request):  #在页面上禁止删除
        return False


admin.site.register(Task,TaskAdmin)
admin.site.register(Result,ResultAdmin)