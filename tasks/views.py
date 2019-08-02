from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTaskForm
from django.contrib.auth.decorators import login_required
from .models import Task, Notification
from datetime import datetime
import datetime as Datetime
# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def new_task(request):
    user = request.user

    if request.method == 'POST':
        post = request.POST.copy()
        d = request.POST['deadline']
        d = d.replace("T", " ")
        d = d + ":00"
        post['deadline'] = d;
        form = NewTaskForm(post)

        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = user
            task.save()
            notification = Notification(time = task.deadline - Datetime.timedelta(days=0, hours=1, minutes=0),
            task=task);
            notification.save();
            return redirect('home')
    else:    
        form = NewTaskForm()

    return render(request, 'new_task.html', {'form' : form})

@login_required
def update_task(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        post = request.POST.copy() or None
        d = request.POST['deadline']
        d = d.replace("T", " ")
        d = d + ":00"
        post['deadline'] = d;
        form = NewTaskForm(post, instance=instance)

        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            Notification.objects.filter(task=task).delete()
            notification = Notification(time=task.deadline - Datetime.timedelta(days=0, hours=1, minutes=0),
            task=task);
            notification.save();
            return redirect('home')
    else:
        form = NewTaskForm(instance=instance)

    return render(request, 'update_task.html', {'form': form}) 

@login_required
def complete_task(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    Notification.objects.filter(task=instance).delete()

    if(instance.repeat == True):
        instance.deadline = instance.deadline + instance.duration
        instance.save()
        notification = Notification(time=instance.deadline - Datetime.timedelta(days=0, hours=1, minutes=0),
        task=instance);
        notification.save();
    else:    
        instance.completed_at = datetime.now()
        instance.save()
    return redirect('home')

@login_required
def remove_task(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    Task.objects.filter(pk=pk).delete()
    return redirect('home')