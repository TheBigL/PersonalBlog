from django.urls import path
from .views import HomeView, PostDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetail.as_view(), name='post-detail')
]