from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from .models import Post


def is_author_or_admin(view_func):
    """
    Decorator to check if the user is the author of the post or an admin.
    If not, return a forbidden response.
    """
    def wrapper_func(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk']) # Get the post instance
        if post.author == request.user or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('You are not authorized to edit this post.')
    
    return wrapper_func