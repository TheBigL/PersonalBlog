from django.urls import re_path
from .views import  UserRegisterView

urlpatterns = [
    re_path(r'members/register', UserRegisterView.as_view(), name="register_user")
    
    
]