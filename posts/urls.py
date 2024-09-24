from django.urls import re_path
from .views import AddPostView, PostDetailView, PostListView, PostEditView, AboutView

urlpatterns = [
    re_path(r'^$', PostListView.as_view()),
    re_path(r'post/<int:pk>/', PostDetailView.as_view()),
    re_path(r'add_post/', AddPostView.as_view()),
    re_path(r'post/edit/<int:pk>/', PostEditView.as_view()),
    re_path(r'post/aboutme/', AboutView.as_view())
    
]