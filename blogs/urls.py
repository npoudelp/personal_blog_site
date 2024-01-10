from django.urls import path
from .views import home, post, search


app_name = 'blogs'

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>', post, name='post'),
    path('search/', search, name='search'),
]