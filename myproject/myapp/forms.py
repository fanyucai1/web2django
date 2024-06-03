from django import forms
from .models import Task,Result
from django.conf import settings
import subprocess,os,re
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields='__all__'
    '''
    def clean_fastq_R1(self):
        fastq_R1 = self.cleaned_data.get("fastq_R1")
        if not fastq_R1.name.endswith('.gz'):
            raise forms.ValidationError("文件格式不正确:fastq.gz or fq.gz")
        return fastq_R1
    '''
class ResultForm(forms.ModelForm):
    class Meta:
        model=Result
        fields = '__all__'