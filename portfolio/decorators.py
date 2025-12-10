from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from .models import Portfolio


def is_admin(view_func):
    """
    Decorator to check if the user is an admin.
    If not, return a forbidden response.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='Admin').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('You are not authorized to perform this action.')
    
    return wrapper_func