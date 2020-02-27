from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.PostList.as_view()),
    path('catlist/',views.CatList.as_view()),
    path('taglist/', views.TagList.as_view()),
    path('comlist/', views.CommentList.as_view()),
    path('shortpost/', views.PostShortList.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('create_post/', views.CreatePost.as_view()),
    path('delete/<id>', views.DeletePost.as_view()),
]
