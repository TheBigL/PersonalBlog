from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'

@login_required
@permission_required('post.add_post', raise_exception=True)
class AddPostView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = 'members/login.html'
    form = PostForm
    success_url = '/'
    template_name = 'addpost.html'
    success_message = "Your post has been created!"
    

class AboutView(TemplateView):
    template_name = "aboutme.html"
    
@login_required
@permission_required('post.update_post', raise_exception=True)
class PostEditView(UpdateView, PermissionRequiredMixin):
    model = Post
    template_name = "editpost.html"
    field = ['title', 'content']






