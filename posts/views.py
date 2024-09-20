from django.views.generic import ListView, GenericView, DetailView
from models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    

class AboutView(GenericView):
    template_name = "about.html"


