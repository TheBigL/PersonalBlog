import pytest
from django.urls import reverse, NoReverseMatch
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from posts.models import Post
from members.models import Member



User = get_user_model()


@pytest.fixture
def test_client():
    """Provides a Django test client."""
    return Client()

@pytest.fixture
def test_superuser(db):
    superuser = User.objects.create_superuser(
        username="testsuperuser",
        email="superuser@example.com",
        password="superpass123",
    )
    return superuser


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
def other_user(db):
    """Creates a second distinct user for ownership tests."""
    user = User.objects.create_user(
        username="otheruser",
        email="other@example.com", # Unique email
        password="password456"
    )
    return user


@pytest.fixture
def contributor_group(db):
    """Creates and returns the 'Contributor' group."""
    group, _ = Group.objects.get_or_create(name="Contributor") # Use get_or_create
    # Ensure the group has the 'add_post' permission
    content_type = ContentType.objects.get_for_model(Post)
    permission, _ = Permission.objects.get_or_create(
        codename="add_post",
        name="Can add post",
        content_type=content_type
    )
    group.permissions.add(permission)
    # Ensure the group has the 'change_post' permission
    return group

@pytest.fixture
def add_post_permission(db):
    """Returns the 'add_post' permission for the Post model."""
    content_type = ContentType.objects.get_for_model(Post)
    permission, _ = Permission.objects.get_or_create(
        content_type=content_type,
        codename="posts.add_post",
        name="Can add post"
    )
   
    return permission

@pytest.fixture
def change_post_permission(db):
    """Returns the 'change_post' permission for the Post model."""
    content_type = ContentType.objects.get_for_model(Post)
    permission, _ = Permission.objects.get_or_create(
        content_type=content_type,
        codename="change_post" # Standard Django codename
    )
    return permission



class TestPermissions:

 
    @pytest.mark.django_db
    def test_add_post_permission(self, test_client, test_user, contributor_group, add_post_permission):
        add_post_url = reverse("posts:add_post")
        post_list_url = reverse("posts:post_list")
        
        #Test 1: Not logged in - Redirect to login
        response_not_logged_in = test_client.get(add_post_url)       
        assert response_not_logged_in.status_code == 302  # Redirect to login

        # Test 2: Logged in
        logged_in = test_client.login(email=test_user.email, password="pass123")
        assert logged_in

        
        # Test 3: Logged in, but without permission
        post_data = {"title": "CBV Post Title", "content": "CBV Post content"}
        response_no_perm = test_client.post(add_post_url, post_data)
        assert response_no_perm.status_code in (302, 403)
        assert Post.objects.count() == 0

        

        # Assign user to the Contributor Group and give them the permission to add posts

         # Ensure permissions are loaded
             # Add to Contributor group
        contributor_group, _ = Group.objects.get_or_create(name="Contributor")
        test_user.groups.add(contributor_group)
        test_user.save()

        # Test 5: Test with permission
        response_with_perm = test_client.post(add_post_url, post_data)
        print(contributor_group.name)
        print(response_with_perm.status_code)
        assert response_with_perm.status_code == 302
        assert response_with_perm.url == post_list_url

        assert Post.objects.count() == 1


    @pytest.mark.django_db
    def test_cannot_view_post_no_login(self, test_client, test_user):
        post = Post.objects.create(title="Test Post", content="Test Content", author=test_user)
        post_detail_url = reverse("posts:post_detail", kwargs={"pk": post.pk})

        # Test 1: Not logged in - Redirect to login
        response_not_logged_in = test_client.get(post_detail_url)
        assert response_not_logged_in.status_code == 200
    
    @pytest.mark.django_db
    def test_edit_post_permission(self, test_client, test_user, contributor_group, change_post_permission):
        initial_post = Post.objects.create(title="Initial Title", content="Initial Content", author=test_user)
        edit_post_url = reverse("posts:edit_post", kwargs={"pk": initial_post.pk})
        post_list_url = reverse("posts:post_list")

        #Create the Contributor group
        contributor_group, _ = Group.objects.get_or_create(name="Contributor")
        test_user.groups.add(contributor_group)
        test_user.save()

        response_not_logged_in = test_client.get(edit_post_url)
        assert response_not_logged_in.status_code == 302  # Redirect to login

        logged_in = test_client.login(email=test_user.email, password="pass123")
        assert logged_in

        updated_data = {"title": "Updated CBV Title", "content": "Updated CBV Content"}

        response = test_client.post(edit_post_url, updated_data)
        assert response.status_code == 302

        initial_post.refresh_from_db()
        print(initial_post.title)
        assert initial_post.title == updated_data["title"]




    
    @pytest.mark.django_db
    def test_cannot_edit_others_post(self, test_client, test_user, other_user, contributor_group, change_post_permission):
        other_post = Post.objects.create(title="Other's Post", content="Content", author=other_user)
        edit_url = reverse("posts:edit_post", kwargs={"pk": other_post.pk})

                #Create the Contributor group
        contributor_group, _ = Group.objects.get_or_create(name="Contributor")
        test_user.groups.add(contributor_group)
        test_user.save()

        logged_in = test_client.login(email=test_user.email, password="pass123")
        assert logged_in

        update_data = {"title": "Attempted Update", "content": "Attempted Update"}
        response = test_client.post(edit_url, update_data)
        assert response.status_code == 403

        other_post.refresh_from_db()
        assert other_post.title == "Other's Post"

    @pytest.mark.django_db
    def test_delete_post_permission(self, test_client, test_user):
        delete_post = Post.objects.create(title="Post to Delete", content="Content", author=test_user)
        delete_url = reverse("posts:delete_post", kwargs={"pk": delete_post.pk})

        contributor_group, _ = Group.objects.get_or_create(name="Contributor")
        test_user.groups.add(contributor_group)
        test_user.save()

        
        logged_in = test_client.login(email=test_user.email, password="pass123")
        assert logged_in

        response = test_client.post(delete_url)  # Use follow=True to follow the redirect
        assert response.status_code in (200, 302)
        assert Post.objects.count() == 0

    @pytest.mark.django_db
    def test_cannot_delete_others_post(self, test_client, test_user, other_user):
        other_post = Post.objects.create(title="Other's Post", content="Content", author=other_user)
        delete_url = reverse("posts:delete_post", kwargs={"pk": other_post.pk})

        #Create the Contributor group
        contributor_group, _ = Group.objects.get_or_create(name="Contributor")
        test_user.groups.add(contributor_group)
        test_user.save()

        logged_in = test_client.login(email=test_user.email, password="pass123")
        assert logged_in



        response = test_client.post(delete_url)
        assert response.status_code == 403

        other_post.refresh_from_db()
        assert other_post.title == "Other's Post"



        
