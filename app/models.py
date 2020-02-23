# Create your models here.
from django.db import models
from django.contrib.auth.models import *
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey

"""class User(AbstractUser):
    модель пользователя для авторизации, логпасс
    class Meta(AbstractUser.Meta):
        swappable="AUTH_USER_MODEL"""
class Cat(MPTTModel):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('url', max_length=100)
    description = models.TextField("Description to category",max_length=100, default="Some_desc", blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name='Parent_category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='Child_category'
    )
    published=models.BooleanField("Otobrazhat?", default=0)
    template = models.CharField(max_length=300, default="blog/sport_list")
    paginated=models.PositiveIntegerField("Kolvo posts on page",default=0)
    sort=models.PositiveIntegerField('Sort', default=0)
    def __str__(self):
        return self.name #корректный вывод имени категории
    class Meta:
        verbose_name="Cat"

class Tag(models.Model):
    name = models.CharField('Tag', max_length=100)
    slug = models.SlugField('Tagslug', max_length=100, unique=True)
    published = models.BooleanField("Otobrazhat?", default=True)

    def __str__(self):
        return  self.name
    class Meta:
        verbose_name='TAG'

class Post(models.Model):
    author = models.ForeignKey(  #модель автора
        User,
        verbose_name="Avtor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title=models.CharField(max_length=30)
    mini_text=models.TextField(max_length=7)
    text=models.TextField(max_length=1000)
    subtitle=models.TextField('Short_desc',max_length=50, blank=True, null=True)
    created_date=models.DateTimeField(auto_now=True)
    slug=models.SlugField('url', max_length=15, unique=True)
    image = models.ImageField("Main image", upload_to="post/", null=True, blank=True)
    edit_date = models.DateTimeField(
        "Date of edit",
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        "Date of publish",
        default=timezone.now,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="Teg", blank=True) #привязка многие ко многим
    category= models.ForeignKey(
        Cat, #первичная модель, для привязки один к одному
        verbose_name='Categors',
        on_delete=models.CASCADE, # что делать при удалении категории
        null=True
    )
    template = models.CharField("Shablon", max_length=100, default='blog/post_detail.html') #выбор шаблона для списка категорий
    published = models.BooleanField("To Publish?", default=True)
    viewed=models.PositiveIntegerField("Was viewed?", default=0)
    status=models.BooleanField("Registered only", default=False)
    sort=models.PositiveIntegerField("To sort", default=0)
    """второй способ подсчёта комментариев, вместо метода в post_details"""
    def get_comments_count(self):
        return self.comment_set.count()
    def get_absolute_url(self): #функция выстраивания url
        return reverse('detail_post', kwargs={'category':self.category.slug, 'slug':self.slug})
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="POST"

class Comment(models.Model):
    author = models.ForeignKey( #обязательно авторизовать для комментария
        User,
        verbose_name="Autor",
        on_delete=models.CASCADE
    )
    text=models.TextField(max_length=50)
    created_date=models.DateTimeField(auto_now_add=True)
    moderation=models.BooleanField()
    post = models.ForeignKey(
        Post,
        verbose_name='Statii',
        on_delete=models.CASCADE,
        #related_name="comments"
    )
    class Meta:
        verbose_name="Commet"






