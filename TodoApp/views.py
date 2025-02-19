from django.shortcuts import render
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