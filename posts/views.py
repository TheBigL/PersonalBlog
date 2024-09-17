from django.shortcuts import render
from .models import Post
# Create your views here.
def HomeView(request):
    posts = Post.objects.all().order_by('date_created')
    return render(request, 'blog.html', {'posts': posts})
    

def PostDetail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'postdetail.html', {'post':post})



