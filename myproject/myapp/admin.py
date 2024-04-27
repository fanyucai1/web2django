from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
# Register your models here.
from .models import Task,Result

admin.site.site_header = '微生物数据分析系统'
admin.site.site_title="123"
admin.site.index_title ="App列表:"

class TaskAdmin(admin.ModelAdmin):
    list_display = ('project','pub_date','fastq_R1','fastq_R2')
    fieldsets = [
        (None, {"fields": ["project"]}),
        ('文件上传', {"fields": ["fastq_R1","fastq_R2"]}),
    ]

class ResultAdmin(admin.ModelAdmin):
    list_display = ('project', 'pub_date')
    def has_add_permission(self, request):#在页面上禁止添加
        return False
    def has_change_permission(self, request):#在页面上禁止修改
        return False
    def has_delete_permission(self, request):  #在页面上禁止删除
        return False


admin.site.register(Task,TaskAdmin)
admin.site.register(Result,ResultAdmin)

