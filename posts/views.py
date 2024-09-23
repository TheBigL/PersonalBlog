from django.views.generic import ListView, View, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'addpost.html'
    

class AboutView(View):
    template_name = "about.html"

class PostEditView(UpdateView):
    model = Post
    template_name = "editpost.html"
    field = ['title', 'content']


