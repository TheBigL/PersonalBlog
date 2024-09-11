from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', views.index, name='index'),
]