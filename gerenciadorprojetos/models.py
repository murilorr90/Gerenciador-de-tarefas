from django.db import models
from django.forms import ModelForm

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	def __unicode__(self):
		return self.title

class Task(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	project_id = models.ForeignKey(Project, null = True)
	def __unicode__(self):
		return self.name

class ProjectForm(ModelForm):
	class Meta:
		model = Project

class TaskForm(ModelForm):
	class Meta:
		model = Task

	fields = ('name','description')	
	
		
