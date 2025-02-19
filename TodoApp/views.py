from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import Task

# Create your views here.

def addTask(request):
    # if request.method=='POST':
    #     return HttpResponse("This is from Form area ")
    # return HttpResponse("this is from Adding task  This is from Home page ")

    formtask=request.POST['task']
    Task.objects.create(task=formtask)
    # return HttpResponse('Data Submitted')
    return HttpResponseRedirect('/')


def mark_as_done(request , pk):

    # return HttpResponse(pk)
    complete=get_object_or_404(Task , pk=pk)
    complete.is_completed=True
    complete.save()

    return redirect('/')

def Delete_Task(request ,pk):
    del_record=get_object_or_404(Task , pk=pk)
    del_record.delete()
    return redirect('/')

def mark_as_undone(request , pk):
    undone=get_object_or_404(Task, pk=pk)
    undone.is_completed=False 
    undone.save()
    return redirect('/')

def update_task(request , pk):
    edit=get_object_or_404(Task , pk=pk)
    # edit.update()
    if request.method=='POST':
        new_task=request.POST['task']
        edit.task=new_task
        edit.save()
        return redirect('/')
    else: 
        context={
            'get_tast':edit
        }
    return render(request, 'edit_task.html' , context)