from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog.html'
    

class PostDetail(DetailView):
    model = Post
    template_name = 'postdetail.html'
