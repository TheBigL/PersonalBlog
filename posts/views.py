from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .forms import PostForm
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

User = get_user_model()
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'

class AboutView(TemplateView):
    template_name = "aboutme.html"
    

class PostEditView(UpdateView, PermissionRequiredMixin):
    model = Post
    template_name = "editpost.html"
    field = ['title', 'content']



def create_post(request):
    form_class = PostForm
    template = 'addpost.html'

    
    if request.method == "POST":
        form = form_class(request.POST)
        title = request.POST.get("title")
        content = request.POST.get("content")
        user_id = request.POST.get("author")

        if request.user.has_perm("posts.add_post"):
            Post.objects.create(
                title=title,
                content=content,
                author=User.objects.get(pk=user_id)
            )
        else:
            pass

    return render(request, template)

def edit_post(request):
    form_class = PostForm
    template = 'editpost.html'

    if request.method == "PATCH":
        form = form_class(request.PATCH)
        Title = request.PATCH.GET("title")
        Content = request.PATCH.GET("content")
        User_id = request.PATCH.GET("author")

    if request.user.has_perm("posts.update_post"):
        Post.objects.update(
            title=Title,
            content=Content,
            author=User.objects.get(pk=User_id)
        )
    else:
        pass

    return render(request, template)


