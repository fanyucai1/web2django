import os.path

from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from .models import Task, Result
import subprocess
from datetime import datetime

@receiver(post_save, sender=Task)
def sync_task_to_result(sender,instance,**kwargs):#同步添加
    try:
        result=Result(project=instance.project,pub_date=instance.pub_date,end_time=datetime.now())
        result.save()
    except Result.DoesNotExist:
        Result.objects.create(project=instance.project, pub_date=instance.pub_date,end_time=datetime.now())

@receiver(pre_delete, sender=Task)
def delete_related_model_b(sender, instance, **kwargs):#同步删除
    result=Result.objects.filter(project=instance.project).delete()
    result.delete()