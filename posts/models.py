from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="post_title", max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="post content")
    date_created = models.DateTimeField(verbose_name="post_date_created", auto_now_add=True)
    date_updated = models.DateTimeField(default=None, verbose_name="post date updated")
