import pytest

from django.contrib.auth import get_user_model

# Create your tests here.
User = get_user_model()

@pytest.fixture()
def user_1(db):
    return User.objects.create_user('user@test.com', 'test')

@pytest.mark.django_db
def test_set_check_password_fail(user_1):
    user_1.set_password("password")
    assert user_1.check_password("wrong") is False


