from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("hello Im from server")

from django.shortcuts import render, redirect, get_object_or_404 
from .models import Task

def task_list(request):
   
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        description = request.POST.get('description')
        create_at =  request.POST.get('create_at')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'task_create.html')

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')  
        task.description = request.POST.get('description')  
        # task.is_completed = request.POST.get('is_completed') == 'on'
        task.save()
        return redirect('task_list')
    return render(request, 'update.html', {'task': task})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')






