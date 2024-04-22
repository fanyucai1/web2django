from django.contrib import admin

# Register your models here.
from .models import task

class taskModelAdmin(admin.ModelAdmin):
    list_display = ('pub_date','user_test')
    search_fields = ('user_test',)
    ordering = ('user_test',)



admin.site.register(task,taskModelAdmin)