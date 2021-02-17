from django.contrib.auth.models import User
from django.db import models



class Project(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    description = models.TextField(max_length=500)
    users = models.ManyToManyField(User,null=True)


class Task(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField()
    weight = models.IntegerField()
    overtime = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)



    @property
    def over(self):
        diff= self.end - self.start
        nbreJours=diff.days

        if(  nbreJours  < self.overtime):
            return True
        if(  nbreJours  >= self.nbreJours):
            return False
        else:
            return None