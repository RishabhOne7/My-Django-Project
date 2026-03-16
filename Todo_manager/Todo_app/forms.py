from django import forms
from Todo_app.models import tasks
class task_forms (forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['Task_Name' , 'status']

        