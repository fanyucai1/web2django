from django.db import models
# Create your models here.
def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.project, filename)

class Task(models.Model):
    project= models.CharField(max_length=100, verbose_name='项目编号',primary_key=True)#primary_key主建
    pub_date=models.DateTimeField(auto_now_add=True,verbose_name="上传时间")
    fastq_R1= models.FileField(upload_to=user_directory_path,verbose_name="R1 fastq")
    fastq_R2= models.FileField(upload_to=user_directory_path,verbose_name="R2 fastq")
    class Meta:
        verbose_name = "1.数据分析"
        verbose_name_plural = "1.数据分析"

class Result(models.Model):
    project = models.CharField(max_length=100, verbose_name='项目编号', primary_key=True)  # primary_key主建
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
    end_time=models.DateTimeField(verbose_name="结束时间")
    class Meta:
        verbose_name = "2.分析结果"
        verbose_name_plural = "2.分析结果"
