from django.db import models

# Create your models here.

class task(models.Model):
    pub_date=models.DateTimeField(verbose_name="时间")
    user_test=models.CharField(verbose_name="用户名",max_length=200)