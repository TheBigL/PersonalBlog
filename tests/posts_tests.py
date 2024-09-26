import pytest
from django.contrib.auth import get_user_model
from posts.models import Post
import factory
from faker import Faker

# Create your tests here.
User = get_user_model()
fake = Faker()

class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name(20)
    email = fake.email()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = fake.text(150)
    author = factory.SubFactory(MemberFactory)
    content = fake.text()

#Fixture

@pytest.fixture()
def contributor(db):
    contributor = User.objects.create_user('contributor@test.com', 'contributor')
    contributor.is_contributor = True
    yield contributor

@pytest.fixture()
def reg(db):
    reg = User.objects.create_user('reg@test.com', 'Regular')
    yield reg

@pytest.mark.django_db
def reg_cannot_post(db):
    new_post = Post.objects.create()
    

