import pytest
import factory
from django.contrib.auth import get_user_model
from factories import MemberFactory
from faker import Faker
from django.urls import reverse
from django.contrib.auth.models import Permission

fake = Faker()

# Create your tests here.
User = get_user_model()




# Basic User to test permission

@pytest.fixture()
def basic_user(db, member_factory):
    user = User.objects.create_user(fake.email(), 'test')
    yield user

@pytest.fixture()
def contributor_user(db):
    contributor = User.objects.create_user('contributor@test.com', 'contributor')
    contributor.is_contributor = True
    yield contributor

@pytest.fixture()
def super_user(db):
    SuperUser = User.objects.create_superuser('superuser', 'superuser@test.com', 'password')
    yield SuperUser



# Basic Tests
class TestMembers:
#Confirms that a user has been created
    @pytest.mark.django_db
    def test_if_user_exists(db):
        user = MemberFactory()
        assert user.username is not None
        assert user.email is not None
    
    # Checks if the password fails
    @pytest.mark.django_db
    def test_set_check_password_fail(db):
    #    basic_user.set_password("password")
        user = MemberFactory()
        assert user.password != 'Wrong' 
    
    # Checks if the password fails
    @pytest.mark.django_db
    def test_set_check_password_success(db):
        user = MemberFactory()
        assert user.password == 'password'
    
    # Checks if the user is not a contributor by default.
    @pytest.mark.django_db
    def test_is_not_contributor_by_default(db):
        user = MemberFactory()
        assert user.is_contributor is False
    
    # Checks if the User is a contributor
    @pytest.mark.django_db
    def test_is_contributor(db):
        user = MemberFactory(is_contributor = True, is_superuser = False)
        assert user.is_contributor is True
    
    # Checks if the user is not a superuser
    @pytest.mark.django_db
    def test_is_not_superuser(db):
        user = MemberFactory()
        assert user.is_superuser is False
    
    # Checks if the user is a superuser
    @pytest.mark.django_db(scope="session")
    def test_is_superuser(db):
        user = MemberFactory(is_superuser = True, is_contributor = True)
        assert user.is_superuser is True