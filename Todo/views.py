from django.http import HttpResponse
from django.shortcuts import render
from TodoApp.models import Task


def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks=Task.objects.filter(is_completed=True)
    # tasks=Task.objects.filter(is_completed=False)
    return render(request , 'home.html' , {'tasks':tasks , 'completed_tasks':completed_tasks})