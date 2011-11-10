# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from gerenciadorprojetos.models import Project, ProjectForm
from gerenciadorprojetos.models import Task, TaskForm
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404


# Project
def project_index(request):
	project_list = Project.objects.all()
	t = loader.get_template('project/index.html')
	c = Context({
		'project_list': project_list,
    	})
    	
	return HttpResponse(t.render(c))

def project_new(request):
	project_form = ProjectForm()
	t = loader.get_template('project/new.html')
	c = Context({'project_form': project_form,})
	return HttpResponse(t.render(c))

def project_create(request):
	formset = ProjectForm(request.POST)
       	if formset.is_valid():
		formset.save()
		return HttpResponseRedirect('/projects/')
	else:
		pass

def project_edit(request,project_id):
	project = get_object_or_404(Project, pk=project_id)
	project_form = ProjectForm(instance=project)
	t = loader.get_template('project/edit.html')
	c = Context({'project_form': project_form,'id':project_id})
	return HttpResponse(t.render(c))

def project_show(request,project_id):
	task_item = Task.objects.all()
	project = get_object_or_404(Project, pk=project_id)
	project_form = ProjectForm(instance=project)
	t = loader.get_template('project/show.html')
	c = Context({'project_form': project_form,'id':project_id,'project':project})
	return HttpResponse(t.render(c))


def project_update(request,project_id):
	project = get_object_or_404(Project, pk=project_id)
	formset = ProjectForm(request.POST, instance=project)
       	if formset.is_valid():
		formset.save()
		return HttpResponseRedirect('/projects/')
	else:
		pass

# Task
def task_index(request,project_id):
	task_list = Task.objects.all()
	t = loader.get_template('task/index.html')
	c = Context({
		'task_list': task_list,
    	})
    	
	return HttpResponse(t.render(c))


def task_new(request,project_id):
	task_form = TaskForm()
	t = loader.get_template('task/new.html')
	c = Context({'task_form': task_form,})
	return HttpResponse(t.render(c))

def task_create(request):
	formset = TaskForm(request.POST)
       	if formset.is_valid():
		formset.save()
		return HttpResponseRedirect('/projects/')
	else:
		pass


def task_edit(request,task_id):
	task = get_object_or_404(Task, pk=task_id)
	task_form = TaskForm(instance=task)
	t = loader.get_template('task/edit.html')
	c = Context({'task_form': task_form,'task_id':task_id})
	return HttpResponse(t.render(c))


def task_update(request,task_id):
	task = get_object_or_404(Task, pk=task_id)
	formset = TaskForm(request.POST, instance=task)
       	if formset.is_valid():
		formset.save()
		return HttpResponseRedirect('/projects/')
	else:
		pass

