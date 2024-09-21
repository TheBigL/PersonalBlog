from django.views.generic import ListView, GenericView, DetailView, CreateView, UpdateView, DeleteView
from models import Post
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
    

class AboutView(GenericView):
    template_name = "about.html"

class PostEditView(UpdateView):
    template_name = "editpost.html"


