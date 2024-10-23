import pytest
import factory
from django.contrib.auth import get_user_model
from posts.models import Post
from factories import MemberFactory, PostFactory
from faker import Faker
from django.contrib.auth.models import Permission

# Create your tests here.
User = get_user_model()
fake = Faker()




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
class TestPosts:
#Disallows user to create a post if they're not a contributor
    @pytest.mark.django_db
    def is_not_contributor(db):
        nonauthorizedUser = MemberFactory()
        can_post = nonauthorizedUser.has_perms("post.add_post")
        assert can_post is False