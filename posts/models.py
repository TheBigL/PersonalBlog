from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="post title", max_length=150,)
    slug = models.SlugField(null=True, blank=True, max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    content = models.TextField(verbose_name="post content",)
    date_created = models.DateTimeField(verbose_name="post date created", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="post date updated", auto_now=True)
    
    class Meta:
        ordering = ["-date_created"]

def __str__(self):
    return self.title

def snippet(self):
    return self.content[:100] + '...'



