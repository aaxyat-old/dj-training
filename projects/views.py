from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projecObj = Project.objects.get(id=pk)

    context = {"project":projecObj}
    return render(request,"projects/project.html", context)


@login_required(login_url="login")
def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")
    context = {"form":form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def update_project(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")
    context = {"form":form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def delete_project(request,pk):
        if request.method == "POST":
            project = Project.objects.get(id=pk)
            project.delete()
            return redirect("projects")
        projectObj=Project.objects.get(id=pk)
        context = {"project":projectObj}
        return render(request, "projects/delete_object.html",context)