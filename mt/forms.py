from django.forms import ModelForm

from api.models import Project,Task


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'start', 'end','description']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'label', 'start','end','weight','overtime','user']
