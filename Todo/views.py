from django.http import HttpResponse
from django.shortcuts import render
from TodoApp.models import Task


def home(request):
    # return HttpResponse('<h1> This is Home of my ToDo Project </h1> ')
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')
    # tasks=Task.objects.filter(is_completed=False)
    return render(request , 'home.html' , {'tasks':tasks})