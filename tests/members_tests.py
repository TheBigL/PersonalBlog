import pytest
import factory
from django.contrib.auth import get_user_model
from factories import MemberFactory
from faker import Faker

fake = Faker()

# Create your tests here.
User = get_user_model()



# Basic User to test permission
'''
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
'''

@pytest.mark.parameterize(
        "email, username, password, is_superuser, is_contributor",
        [
            ('email@test.ca', 'testuser', 'password', False, False),
            ('contributor@test.ca', 'testuser', 'password', False, True),
            ('superuser@test.ca', 'testuser', 'password', True, True),

        ] 
)

# Basic Tests

#Confirms that a user has been created
@pytest.mark.django_db
def test_if_user_exists(member_factory):
    user = member_factory.create()
    assert User.objects.count() > 0

# Checks if the password fails
@pytest.mark.django_db
def test_set_check_password_fail(member_factory):
#    basic_user.set_password("password")
    user = member_factory.create()
    
    
    
    assert basic_user.check_password("wrong") is False

# Checks if the password fails
@pytest.mark.django_db
def test_set_check_password_success(basic_user):
    basic_user.set_password("password")
    assert basic_user.check_password("password") is True

# Checks if the user is not a contributor by default.
@pytest.mark.django_db
def test_is_not_contributor_by_default(basic_user):
    assert basic_user.is_contributor is False

# Checks if the User is a contributor
@pytest.mark.django_db
def test_is_contributor(contributor_user):
    assert contributor_user.is_contributor is True

# Checks if the user is not a superuser
@pytest.mark.django_db
def test_is_not_superuser(basic_user):
    assert basic_user.is_superuser is False

# Checks if the user is a superuser
@pytest.mark.django_db
def test_is_superuser(super_user):
    assert super_user.is_superuser is True