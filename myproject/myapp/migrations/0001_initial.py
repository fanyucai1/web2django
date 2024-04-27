# Generated by Django 5.0.4 on 2024-04-27 04:17

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('project', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='项目编号')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '2.分析结果',
                'verbose_name_plural': '2.分析结果',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('project', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='项目编号')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('fastq_R1', models.FileField(upload_to=myapp.models.user_directory_path, verbose_name='R1 fastq')),
                ('fastq_R2', models.FileField(upload_to=myapp.models.user_directory_path, verbose_name='R2 fastq')),
            ],
            options={
                'verbose_name': '1.数据分析',
                'verbose_name_plural': '1.数据分析',
            },
        ),
    ]
