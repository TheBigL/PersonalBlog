from typing import Any
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.utils import timezone

# Create your models here.
class Member(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You've failed to provide your email")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    class Members(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        is_contributor = models.BooleanField(default=False)
        date_joined = models.DateTimeField(default=timezone.now)


