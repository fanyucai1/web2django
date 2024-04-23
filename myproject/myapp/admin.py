from django.contrib import admin

# Register your models here.
from .models import task

class taskModelAdmin(admin.ModelAdmin):
    list_display = ('project','pub_date','fastq_R1','fastq_R2')

admin.site.register(task,taskModelAdmin)