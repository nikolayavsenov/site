from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view()),
    path('catlist/',views.CatList.as_view()),
    path('taglist/', views.TagList.as_view()),
    path('comlist/', views.CommentList.as_view()),
    path('shortpost/', views.PostShortList.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('create_post/', views.CreatePost.as_view())
]
