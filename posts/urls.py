from django.urls import re_path
from .views import PostDetailView, PostListView, AddPostView, EditPostView, AboutView, HomepageView, DeletePostView 
app_name = 'posts'

urlpatterns = [
    re_path(r'^$', PostListView.as_view(), name="post_list"),
    re_path(r'^posts/add_post/', AddPostView.as_view(), name="add_post"),
    re_path(r'^posts/post_detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post_detail"),
    re_path(r'^posts/edit_post/(?P<pk>\d+)/$', EditPostView.as_view(), name="edit_post"),
    re_path(r'^posts/delete_post/(?P<pk>\d+)/$', DeletePostView.as_view(), name="delete_post"),
    re_path(r'^posts/aboutme/', AboutView.as_view(), name="about_us"),
    re_path(r'^homepage/$', HomepageView.as_view(), name="homepage")
    
]