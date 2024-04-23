from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    return 'user_data/{0}/{1}'.format(instance.project, filename)


class task(models.Model):
    project= models.CharField(max_length=100, verbose_name='项目编号')
    pub_date=models.DateTimeField(auto_now_add=True,verbose_name="上传时间")
    fastq_R1= models.FileField(upload_to=user_directory_path,verbose_name="R1 fastq")
    fastq_R2= models.FileField(upload_to=user_directory_path,verbose_name="R2 fastq")
    class Meta:
        verbose_name = "数据分析"
        verbose_name_plural = "数据分析"