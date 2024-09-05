import pytest

from django.contrib.auth import get_user_model

# Create your tests here.
User = get_user_model()

@pytest.fixture()
def basic_user(db):
    return User.objects.create_user('user@test.com', 'test')


@pytest.mark.django_db
def test_if_user_exists(basic_user):
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_set_check_password_fail(basic_user):
    basic_user.set_password("password")
    assert basic_user.check_password("wrong") is False


@pytest.mark.django_db
def test_set_check_password_success(basic_user):
    basic_user.set_password("password")
    assert basic_user.check_password("password") is True