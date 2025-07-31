from django.urls import re_path
from .views import  RegisterUser, LoginUser

app_name = 'members'

urlpatterns = [
    
    re_path(r'^members/register/$', RegisterUser.as_view(), name="register"),
    re_path(r'^members/login/$', LoginUser.as_view(), name="login"),
    
    
    
]