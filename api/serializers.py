from rest_framework import serializers
from .models import Project,Task

'''CREATION DE POST SERIALIZER'''
class ProjectSerializer(serializers.ModelSerializer):
    '''ordonnees les attribues du model'''
    class Meta:
        model = Project
        fields = ['id','name','start','end','description']

    '''afficher les nombres de votes'''
    def get_projects(self, project):
        return Project.objects.filter(name=project).count()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','project','label','start','end','weight','overtime']
