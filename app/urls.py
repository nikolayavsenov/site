from django.contrib import admin
from django.urls import path, include
from app.views import *
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('<slug:category_name>/', views.CatView.as_view(), name="category"),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name="detail_post")
]