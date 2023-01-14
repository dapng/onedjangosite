from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddPostForm
from .models import Human
from .utils import DataMixin, menu


class HumanHome(DataMixin, ListView):
    model = Human
    template_name = 'human/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main page')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Human.objects.filter(is_published=True)


def about(request):
    return render(
        request,
        'human/about.html',
        {'menu': menu, 'title': 'About page'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'human/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add page')
        return dict(list(context.items()) + list(c_def.items()))


def contact(reauest):
    return HttpResponse('Contact page')


def login(request):
    return HttpResponse('Login page')


class ShowPost(DataMixin, DetailView):
    model = Human
    template_name = 'human/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class HumanCategory(DataMixin, ListView):
    model = Human
    template_name = 'human/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Human.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
