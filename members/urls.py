from django.urls import re_path
from .views import  RegisterUser, LoginUser

urlpatterns = [
    
    re_path(r'^$', RegisterUser.as_view(), name="register_user"),
    re_path(r'^register/$', RegisterUser.as_view(), name="register"),
    re_path(r'^login/$', LoginUser.as_view(), name="login_user"),
    
    
    
]