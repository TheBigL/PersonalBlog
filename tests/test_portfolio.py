import pytest
from django.urls import reverse, NoReverseMatch
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from portfolio.models import Portfolio
from members.models import Member


User = get_user_model()


@pytest.fixture
def test_client():
    """Provides a Django test client."""
    return Client()

class TestPortfolioPermissions:

    @pytest.mark.django_db
    def test_create_portoflio():
        add_portfolio_url = reverse()
        return None