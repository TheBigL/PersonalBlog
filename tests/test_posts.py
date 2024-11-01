import pytest
from django.contrib.auth import get_user_model
from posts.models import Post
from members.models import Member
from factories import MemberFactory, PostFactory
from faker import Faker
from django.contrib.auth.models import Group

# Create your tests here.
User = get_user_model()
fake = Faker()





#Fixture
@pytest.fixture(scope="session")
def contributor_group(db):
    return Group.objects.create("Contributor")



@pytest.fixture(scope="session")
def authorized_user(db):
    authorized_user = MemberFactory()
    return authorized_user


 

# Post Tests
class TestPosts:
#Disallows user to create a post if they're not a contributor
    @pytest.mark.django_db
    def test_is_not_contributor(db):
        reg = MemberFactory()
        
        assert reg.has_post_permissions() is False
#Allows a user to create a post if they're a contributor.     



        