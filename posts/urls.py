from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.HomeView, name="homeblog"),
    re_path(r'(?P<slug>)[])', views.PostDetail)
]