from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse


user = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="post title", max_length=150,)
    slug = models.SlugField(null=True, blank=True, max_length=250)
    author = models.ForeignKey(user, on_delete=models.CASCADE,)
    content = models.TextField(verbose_name="post content",)
    date_created = models.DateTimeField(verbose_name="post date created", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="post date updated", auto_now=True)
    
    class Meta:
        ordering = ["-date_created"]
        permissions = [
            ("create_post", "Can add post"),
            ("edit_post", "Can change post"),
            ("remove_post", "Can delete post"),
        ]
        

def __str__(self):
    return self.title

def is_author_contributor(self):
    if self.author.is_contributor:
        self.save()

def get_absolute_url(self):
    return reverse("posts:post_detail", kwargs={"pk": self.pk})




def snippet(self):
    return self.content[:100] + '...'



