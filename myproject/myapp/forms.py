from django import forms
from .models import Task
import re
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields='__all__'
    def clean_fastq_R1(self):
        fastq_R1=self.cleaned_data['fastq_R1']
        if not re.search(r'.gz$',fastq_R1):
            print('no good')
            raise forms.ValidationError("no good")
        return fastq_R1