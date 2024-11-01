import factory
from faker import Faker
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth import get_user_model
from posts.models import Post
from members.models import Member
fake = Faker()
User = get_user_model()

class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = 'password'
    is_active = True
    is_superuser = False
    
    @classmethod
    def has_post_permissions(self):
        self.has_post_permissions()

    


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = fake.text(150)
    author = factory.SubFactory(MemberFactory)
    content = fake.text()