from django.urls import path

from .views import about, contact, login, AddPage, HumanHome, HumanCategory, ShowPost

urlpatterns = [
    path('', HumanHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', HumanCategory.as_view(), name='category')
]
