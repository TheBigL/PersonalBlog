from django.urls import re_path
from .views import PostDetailView, PostListView, PostEditView, AboutView
from . import views
urlpatterns = [
    re_path(r'^$', PostListView.as_view()),
    re_path(r'post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    re_path(r'add_post/', views.create_post, name="add_post"),
    re_path(r'edit_post/<int:pk>/', views.edit_post, name="edit_post"),
    re_path(r'post/aboutme/', AboutView.as_view(), name="about_us")
    
]