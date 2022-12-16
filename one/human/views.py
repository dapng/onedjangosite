from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


menu = ['test 1', 'test 2', 'test 3', 'test 4', 'test 5']


def index(request):
    posts = Human.objects.all()
    return render(request, 'human/index.html', {'posts': posts ,'menu': menu, 'title': 'Main page'})


def about(request):
    return render(request, 'human/about.html', {'menu': menu, 'title': 'About page'})


def catigories(request, cat):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Article is:</h1><p>{cat}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Archive fron year:</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>page not found</h1>')
