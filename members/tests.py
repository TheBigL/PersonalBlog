import pytest
from django.contrib.auth import get_user_model

# Create your tests here.
User = get_user_model()
# Basic User to test permission
@pytest.fixture()
def basic_user(db):
    user = User.objects.create_user('user@test.com', 'test')
    yield user

@pytest.fixture()
def contributor_user(db):
    contributor = User.objects.create_user('contributor@test.com', 'contributor')
    contributor.is_contributor = True
    yield contributor

@pytest.fixture()
def super_user(db):
    SuperUser = User.objects.create_user('superuser', 'superuser@test.com', 'myPassword')
    SuperUser.is_superuser = True
    SuperUser.is_active = True
    SuperUser.is_contributor = True
    yield SuperUser
    print('\n Deleting Superuser...')
    
# Basic Tests
#Confirms that a user has been created
@pytest.mark.django_db
def test_if_user_exists(basic_user):
    assert User.objects.count() > 0

# Checks if the password fails
@pytest.mark.django_db
def test_set_check_password_fail(basic_user):
    basic_user.set_password("password")
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

@pytest.mark.django_db
def test_is_contributor(contributor_user):
    assert contributor_user.is_contributor is True

@pytest.mark.django_db
def test_is_not_superuser(basic_user):
    assert basic_user.is_superuser is False

@pytest.mark.django_db
def test_is_superuser(super_user):
    assert super_user.is_superuser is True