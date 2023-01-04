from django.urls import path

from .views import about, add_page, contact, login, show_post, show_category, HumanHome

urlpatterns = [
    path('', HumanHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category')
]
