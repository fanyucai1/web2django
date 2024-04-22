from django.db import models

# Create your models here.

class task(models.Model):
    number = models.AutoField(primary_key=True, verbose_name='编号')
    pub_date=models.DateTimeField(verbose_name="时间")
    user_test=models.CharField(verbose_name="用户名",max_length=200)
    class Meta:
        verbose_name = "数据分析任务"
        verbose_name_plural = "数据分析任务"
