from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
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
    

class AboutView(TemplateView):
    template_name = "aboutme.html"
    

class PostEditView(UpdateView):
    model = Post
    template_name = "editpost.html"
    field = ['title', 'content']


