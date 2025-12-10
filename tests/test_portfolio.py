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

@pytest.fixture
def test_user(db):
    """Creates and returns a standard test user using the MemberManager."""
    # Uses the custom MemberManager's create_user
    user = User.objects.create_user(
        username="testuser",
        email="test@example.com", # Make sure email is unique if running multiple tests
        password="pass123"
    )
    group = Group.objects.get_or_create(name="Member")
    user.groups.add(group[0])  # Add the user to the 'Member' group
      # Set the user as a contributor
    user.save()  # Save the user to apply changes
    return user

class TestPortfolioPermissions:

    @pytest.mark.django_db
    def test_create_portoflio():
        add_portfolio_url = reverse("portfolio:add_portfolio")
        portfolio_list_url = reverse("portfolio:portfolio_list")

        response = test_client.get(add_portfolio_url)
        assert response.status_code == 302  # Redirect to login
        
        logged_in = test_client.login(email=test_user.email, password="pass123")
        assert logged_in

        post_data = {"title": "My Portfolio", "description": "Portfolio Description", "link": "http://example.com"}
        response = test_client.post(add_portfolio_url, data=post_data)
        assert response.status_code == 302  # Redirect after successful creation
        assert response.url == portfolio_list_url

        admin_group = Group.objects.get_or_create(name="Admin")
        test_user.groups.add(admin_group)
        test_user.save()

        reponse_with_perm = test_client.post(add_portfolio_url, post_data)
        assert reponse_with_perm.status_code == 302
        assert reponse_with_perm.url == portfolio_list_url

        assert Portfolio.objects.count() == 1


        
