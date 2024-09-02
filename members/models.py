from django.contrib.auth.models import User, UserManager, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models



# Create a new User

# Create a superuser

class MemberManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("You must have an email address in order to register")
        if not username:
            raise ValueError("You must have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_contributor = True
        user.save(using=self._db)
        return user

def get_profile_image_filepath(self, filename):
    return f'profile_images/{str(self.pk)}/{"profile_image.png"}'

# Create your models here.
class Member(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=45, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to='images/pfps/', null=True, blank=True)
    is_contributor = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name = 'Memeber'
        verbose_name_plural = 'Members'

    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.name.split('@')[0]
    
