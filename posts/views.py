from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from members.decorators import allowed_users
from .decorators import is_author_or_admin
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator

User = get_user_model()
# Create your views here.

# Example: A basic list view if needed for redirects
class HomepageView(TemplateView):
    template_name = 'homepage.html'  # Example template name


class PostListView(ListView):
    model = Post
    template_name = 'blog.html' # Example template name
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'

class AboutView(TemplateView):
    template_name = "aboutme.html"
    




@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['Admin', 'Contributor']), name='dispatch')
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/addpost.html'
    success_url = reverse_lazy('posts:post_list')

   
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)





    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to add a post.")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully!")
        return super().form_valid(form)
    


@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['Admin', 'Contributor']), name='dispatch')
@method_decorator(is_author_or_admin, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/edit_post.html'
    permission_required = 'posts.change_post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author = self.request.user)

    def get_success_url(self):
        return reverse('posts:post_list')
    
        
    
@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['Admin', 'Contributor']), name='dispatch')
@method_decorator(is_author_or_admin, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('posts:post_list')

            
        


