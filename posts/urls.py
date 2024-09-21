from django.urls import include, re_path
from views import AboutView, AddPostView, CreateView, DetailView, PostDetailView, PostListView, PostEditView

urlpatterns = [
    re_path(r'^$', PostListView.as_view, name="homeblog"),
    re_path(r'about', AboutView.as_view),
    re_path(r'post/<int:pk>', PostDetailView.as_view),
    re_path(r'add_post/', AddPostView.as_view, name="Add Post"),
    re_path(r'post/edit/<int:pk>', PostEditView.as_view)
    
]