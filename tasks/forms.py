from django import forms
from django.core.validators import MinValueValidator
# from django.utils.translation import gettext_lazy as _
from .models import Task
import datetime

class NewTaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(label='Deadline', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    repeat = forms.BooleanField(required=False, label='Want to repeat the task?', widget=forms.CheckboxInput(attrs={'style': 'width: 2%;'}))
    duration = forms.DurationField(initial=datetime.timedelta(days=1, hours=0), required=False, label='Repeat After', help_text="days hh:mm:ss", validators=[MinValueValidator(datetime.timedelta(days=0, hours=0, minutes=5))])

    class Meta:
        model = Task
        fields = ('name', 'description', 'deadline', 'repeat', 'duration')
    