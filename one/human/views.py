from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import AddPostForm
from .models import Human


menu = [
    {'title': 'Info', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'},
]


class HumanHome(ListView):
    model = Human
    template_name = 'human/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Human.objects.filter(is_published=True)


def about(request):
    return render(
        request,
        'human/about.html',
        {'menu': menu, 'title': 'About page'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'human/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context


def contact(reauest):
    return HttpResponse('Contact page')


def login(request):
    return HttpResponse('Login page')


class ShowPost(DetailView):
    model = Human
    template_name = 'human/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


class HumanCategory(ListView):
    model = Human
    template_name = 'human/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Human.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория -' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>page not found</h1>')
