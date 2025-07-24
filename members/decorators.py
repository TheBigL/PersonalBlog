from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseForbidden



def unauthenticated_user(view_func):
    """
    Decorator to check if the user is authenticated.
    If the user is authenticated, redirect them to the home page.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    """
    Decorator to check if the user has one of the allowed roles.
    If not, return a forbidden response.
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if(request.user.groups.filter(name__in=allowed_roles).exists() or request.user.is_superuser):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden('You are not authorized to view this page.')
        
        return wrapper_func
    
    return decorator
