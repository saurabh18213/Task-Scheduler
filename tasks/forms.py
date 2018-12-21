from django import forms
# from django.utils.translation import gettext_lazy as _
from .models import Task

class NewTaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(label='Deadline', help_text="yy-mm-dd hr:min:sec")

    class Meta:
        model = Task
        fields = ('description', 'deadline')

        