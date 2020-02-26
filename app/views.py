from datetime import datetime
from django.http import HttpResponse, Http404
from .models import *
from django.template import loader
from django.views.generic.base import View
from django.template.loader import *
from django.shortcuts import render, get_object_or_404,redirect
from .forms import CommentForm


"""def home(request):
    if request.method== "POST":
        return HttpResponse('QQ')
    else:
        return HttpResponse(' No qq')

class HomeView(View):
    def get(self, request):
        Cat_list = Cat.objects.all()# передаёт параметры для рендера страницы, словарь или список
        отображаем разрешенные к публикации и сравниваем текущую дату с датой публикации
        post_list=Post.objects.filter(published_date__lte=datetime.now(), published=True)
        #post_list тут для вывода постов
        return render(request, 'blog/post_list.html', {'categories': Cat_list, 'post_list': post_list})
"""
class PostDetailView(View):
    "Fully post rend"
    def get(self, request, **kwargs): #kwargs указали дабы принимать category и строить нормальный url
        category_list = Cat.objects.filter(published=True)  # передаёт параметры для рендера страницы, словарь или список
        post = get_object_or_404(Post, slug=kwargs.get('slug')) # выводим только тот, который нам передала страница в slug
        form=CommentForm()
        #можно обратиться к названию поля в таблице, post_id
        #comments = Comment.objects.filter(post_id=post)#(post=post)
        return render(request, 'blog/post_detail.html', {
            'categories': category_list,
            'post': post,
            'form': form,
            # 'comments': comments
        })

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get('slug'))
            form.author = request.user
            form.save()
        return redirect(request.path) #возвращаем на ту же страницу
""" Старые классы
class CatView(View):
    def get(self,request, category_name):
        posts = Post.objects.filter(
            #обращаемся к Cat и фильтруем нужные категории
            category__slug=category_name, category__published=True, published=True
        ) #выводим только выбранные категории
        return render(request, posts.first().get_category_template(), {'post_list': posts})

class TagView(View):
    def get(self, request, slug):
        posts = Post.objects.filter(tags__slug=slug, published=True) #для использования одного шаблона на разные выводы
        #тут post_list для вывода тегов
        return render(request, posts.first().get_category_template, {'post_list': posts})"""

class PostListView(View):
    def get_queryset(self):#функция проверки актуальности поста
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)
    def get(self, request, category_slug=None, slug=None):
       # category_list = Cat.objects.filter(published=True)  # передаёт параметры для рендера страницы, словарь или список
        # на основании полученного параметра ниже будет алгоритм отображения
        if category_slug is not None:
            posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)#обращаемся к Cat и фильтруем нужные категории
         #выводим только выбранные категории
        elif slug is not None:
            posts = self.get_queryset().filter(tags__slug=slug, tags__published=True)
        else:
            posts = self.get_queryset()
        if posts.exists(): #если посты в категории есть, то ренлерим стандартный шаблон,иначе выводим общий список постов
            template=posts.first().get_category_template()
        else:
            #template='blog/post_list.html'
            raise Http404() #Кидаем 404, если не нашли статьи/категории
        return render(request, template, {'post_list': posts,})

    """class CreateCommentView(View):
        Создание комментария
        def post(self, request, pk):
            form = CommentForm(request.POST)
            if form.is_valid():
                form=form.save(commit=False)
                form.post_id=pk
                form.author=request.user
                form.save()
            return HttpResponse(status=201)"""




