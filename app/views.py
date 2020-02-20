from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.views.generic.base import View

"""def home(request):
    if request.method== "POST":
        return HttpResponse('QQ')
    else:
        return HttpResponse(' No qq')"""

class HomeView(View):
    def get(self, request):
        Cat_list = Cat.objects.all()# передаёт параметры для рендера страницы, словарь или список
        """отображаем разрешенные к публикации и сравниваем текущую дату с датой публикации"""
        post_list=Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request, 'blog/post_list.html', {'categories': Cat_list, 'posts': post_list})

class PostDetailView(View):
    "Fully post rend"
    def get(self, request, category, slug):
        Cat_list = Cat.objects.all()  # передаёт параметры для рендера страницы, словарь или список
        post = Post.objects.get(slug=slug) # выводим только тот, который нам передала страница в slug
        return render(request, 'blog/post_detail.html', {'categories': Cat_list, 'post': post})

class CatView(View):
    def get(self,request, category_name):
        category = Cat.objects.get(slug=category_name) #выводим только выбранные категории
        return render(request, 'blog/post_list.html', {'category': category})

