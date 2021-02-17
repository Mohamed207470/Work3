from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView

from api.models import Project, Task


class ProjectCreate(CreateView):

    # specify the model for create view
    model = Project

    # specify the fields to be displayed

    fields = ['name', 'start','end','description']

class TaskCreate(CreateView):
    model = Task
    fields = ['project', 'label','start','end','weight','overtime']



