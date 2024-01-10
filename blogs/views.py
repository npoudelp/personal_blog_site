from django.shortcuts import render
from .models import post as posts

# Create your views here.


def home(request):
    blogs = posts.objects.filter(status='publish').order_by('-id')
    res = {
        'blogs':blogs,
    }
    return render(request, 'home.html', res)


def post(request, id):
    one_post = posts.objects.get(id=id)
    res = {
        'blog':one_post,
    }
    return render(request, 'post.html', res)


def search(request):
    key = request.POST.get('key')
    blogs = posts.objects.filter(title__contains=key) | posts.objects.filter(blog__contains=key)

    res = {
        'blogs':blogs,
    }
    return render(request, 'home.html', res)