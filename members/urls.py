from django.urls import re_path
from .views import  SignUpView

urlpatterns = [
    re_path(r'members/register', SignUpView.as_view(), name="register_user")
    
    
]