"""
Views for Task Manager application.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Project, Task, Tag
from .forms import RegisterForm, ProjectForm, TaskForm, CustomLoginForm


def home(request):
    """Home page - landing for authenticated and anonymous users."""
    if request.user.is_authenticated:
        projects = Project.objects.filter(owner=request.user)[:5]
        return render(request, 'tasks/home.html', {'projects': projects})
    return render(request, 'tasks/home.html')


class CustomLoginView(LoginView):
    """Custom login view with redirect."""
    template_name = 'tasks/login.html'
    form_class = CustomLoginForm
    redirect_authenticated_user = True


def register_view(request):
    """User registration view."""
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})


def logout_view(request):
    """Logout view."""
    logout(request)
    return redirect('home')


@login_required
def project_list(request):
    """List all projects for the current user."""
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'tasks/project_list.html', {'projects': projects})


@login_required
def project_detail(request, pk):
    """Project detail with its tasks."""
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = project.tasks.all()
    return render(request, 'tasks/project_detail.html', {'project': project, 'tasks': tasks})


@login_required
def project_create(request):
    """Create a new project."""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_form.html', {'form': form, 'action': 'Create'})


@login_required
def project_update(request, pk):
    """Update an existing project."""
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'tasks/project_form.html', {'form': form, 'project': project, 'action': 'Update'})


@login_required
def project_delete(request, pk):
    """Delete a project."""
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'tasks/project_confirm_delete.html', {'project': project})


@login_required
def task_create(request, project_pk):
    """Create a new task in a project."""
    project = get_object_or_404(Project, pk=project_pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            form.save_m2m()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'project': project, 'action': 'Create'})


@login_required
def task_update(request, project_pk, pk):
    """Update an existing task."""
    project = get_object_or_404(Project, pk=project_pk, owner=request.user)
    task = get_object_or_404(Task, pk=pk, project=project)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'project': project, 'task': task, 'action': 'Update'})


@login_required
def task_delete(request, project_pk, pk):
    """Delete a task."""
    project = get_object_or_404(Project, pk=project_pk, owner=request.user)
    task = get_object_or_404(Task, pk=pk, project=project)
    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', pk=project.pk)
    return render(request, 'tasks/task_confirm_delete.html', {'project': project, 'task': task})
