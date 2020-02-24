from django.contrib import admin
from django.urls import path, include
from app.views import *
from . import views

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('tag/<slug:slug>/', views.PostListView.as_view(), name='tag'),
    path('<slug:category_slug>/', views.PostListView.as_view(), name="category"),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name="detail_post")
]