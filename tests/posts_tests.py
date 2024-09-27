import pytest
import factory
from django.contrib.auth import get_user_model
from posts.models import Post
from factories import MemberFactory, PostFactory
from faker import Faker

# Create your tests here.
User = get_user_model()
fake = Faker()
user = MemberFactory(is_contributor = True, is_superuser = True)


#Fixture
'''
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
'''    

# Post Tests

#Disallows user to 