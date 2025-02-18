from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('<h1> This is Home of my ToDo Project </h1> ')
    return render(request , 'home.html')