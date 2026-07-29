import pytest
from django.urls import reverse
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

@pytest.fixture
def admin_group(db):
    group, _ = Group.objects.get_or_create(name="Admin")
    content_type = ContentType.objects.get_for_model(Portfolio)
    add_permissions, _ = Permission.objects.get_or_create(
        codename='add_portfolio',
        name='Can add portfolio',
        content_type=content_type
    )
    group.permissions.add(add_permissions)
    return group

@pytest.fixture
def add_portfolio_permission(db):
    content_type = ContentType.objects.get_for_model(Portfolio)
    permission, _ = Permission.objects.get_or_create(
        content_type = content_type,
        codename = "add_portfolio",
    )
    return permission

@pytest.fixture
def change_portfolio_permission(db):
    content_type = ContentType.objects.get_for_model(Portfolio)
    permission, _ = Permission.objects.get_or_create(
        content_type = content_type,
        codename = "change_portfolio",
    )
    return permission

class TestPortfolio:

    @pytest.mark.django_db
    def test_create_portfolio(self, test_client, test_user):
        add_portfolio_url = reverse("portfolio:add_portfolio")
        portfolio_list_url = reverse("portfolio:portfolio_list")

        response_not_logged_in = test_client.get(add_portfolio_url)
        assert response_not_logged_in.status_code == 302  # Redirect to login
        
        logged_in = test_client.login(email=test_user.email, password="pass123")
        assert logged_in

        post_data = {"name": "My Portfolio", "description": "Portfolio Description", "link": "http://example.com"}
        response_no_perm = test_client.post(add_portfolio_url, data=post_data)
        assert response_no_perm.status_code == 403  # Redirect after successful creation
        assert Portfolio.objects.count() == 0

        admin_group, _ = Group.objects.get_or_create(name="Admin")
        test_user.groups.add(admin_group)
        test_user.save()
        
        

        response_with_perm = test_client.post(add_portfolio_url, data=post_data)
        assert response_with_perm.status_code == 302
        print(response_with_perm)

        assert Portfolio.objects.count() == 1


        
    @pytest.mark.django_db
    def test_cannot_create_portfolio_unless_admin(self, test_client, test_user):
        add_portfolio_url = reverse("portfolio:add_portfolio")

        response = test_client.get(add_portfolio_url)
        assert response.status_code == 302  # Redirect to login
        
        logged_in = test_client.login(email=test_user.email, password="pass123")
        assert logged_in

        post_data = {"name": "My Portfolio", "description": "Portfolio Description", "link": "http://example.com"}
        response = test_client.post(add_portfolio_url, data=post_data)
        assert response.status_code == 403  # Forbidden

        assert Portfolio.objects.count() == 0

    @pytest.mark.django_db
    def test_edit_portfolio(self, test_client, test_user):
        initial_port = Portfolio.objects.create(name="Initial Portfolio", description="Initial Description", link="intial.ca")

        edit_portfolio_url = reverse("portfolio:edit_portfolio", kwargs={"pk": initial_port.pk})
        portfolio_detail_url = reverse("portfolio:portfolio_detail", kwargs={"pk": initial_port.pk})


        logged_in = test_client.login(email=test_user.email, password="pass123")
        assert logged_in
        
        updated_data = {"name": "Updated Portfolio", "description": "Updated Description", "link": "updated.ca"}

        response = test_client.post(edit_portfolio_url, data=updated_data)
        assert response.status_code == 302  # Redirect after successful edit
        
        initial_port.refresh_from_db()
        print(initial_port.name)
        assert initial_port.name == updated_data["name"]