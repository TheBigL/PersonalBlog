from django.urls import path
from . import views

urlpatterns = [
    path('memebers/', views.members, name='members'),
]