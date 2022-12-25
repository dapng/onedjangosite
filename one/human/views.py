from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import Human, Category


menu = [
    {'title': 'Info', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'},
]


def index(request):
    posts = Human.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0}
    return render(request, 'human/index.html', context=context)


def about(request):
    return render(
        request,
        'human/about.html',
        {'menu': menu, 'title': 'About page'})


def add_page(request):
    return HttpResponse('Add page')


def contact(reauest):
    return HttpResponse('Contact page')


def login(request):
    return HttpResponse('Login page')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def show_category(request, cat_id):
    posts = Human.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id}
    return render(request, 'human/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>page not found</h1>')
