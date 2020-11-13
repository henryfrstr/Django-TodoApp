from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, UpdateTaskForm

def list_create_tasks(request):
    queryset = Task.objects.all()
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = TaskForm()
        return redirect('.')
    context = {
        'queryset': queryset,
        'form': form
    }
    return render(request, "todo/task_list_create.html", context)

def update_task(request, id):
    obj = get_object_or_404(Task, id=id)
    form = UpdateTaskForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_tasks')
    context = {
        'form': form
    }
    
    return render(request, "todo/task_update.html", context)

def delete_task(request, id):
    obj = obj = get_object_or_404(Task, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_tasks')
    context = {
        'obj': obj
    }
    
    return render(request, "todo/task_delete.html", context)