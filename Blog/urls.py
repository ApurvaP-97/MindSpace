from django.contrib import admin
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views
from django.urls import path


#File to add routes. 
#home route is here. The logic at PostListView() will be displayed
#why name : For some kind of reverse look up
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #home page is empty path. Naming it as just home might collide with homes of other apps in the project
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'), #<name of model>_<form> -> UpdateView needs the same template too.
	path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
	path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
	path('about/', views.about, name='blog-about'),
	path('helpline/',views.helpline,name='helpline')
]

