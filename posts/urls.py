from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.HomeView, name="homeblog"),
    re_path(r'post/<int:pk>', views.PostDetail),
    re_path(r'add_post/', views.AddPost, name="Add Post"),
    re_path(r'post/edit/<int:pk>')
    
]