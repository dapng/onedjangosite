from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Test human page')


def catigories(request, cat):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Article is:</h1><p>{cat}</p>')

def archive(request, year):
    return HttpResponse(f'<h1>Archive fron year:</h1><p>{year}</p>')