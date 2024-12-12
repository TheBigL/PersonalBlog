import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from posts.models import Post

User = get_user_model()


class TestPermissions:
    @pytest.mark.django_db
    def test_post_add_contributor_group_permission(db):
        client = Client()

        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="pass123"
        )

        

        post_data = {
            "title": "Post Title",
            "content": "Post Content",
            "author": user.id
        }

        group = Group.objects.create(name="Contributor")
        client.login(username="testuser", password="pass123")

        response = client.post(reverse("add_post"), post_data)

        assert response.status_code == 200
        assert Post.objects.all().count() == 0

        content_type = ContentType.objects.get_for_model(Post)
        permission = Permission.objects.get(
            content_type=content_type,
            codename__icontains="add"
        )

        group.permissions.add(permission)
        user.groups.add(group)

        response = client.post(reverse("add_post"), post_data)

        assert response.status_code == 200
        assert Post.objects.all().count() == 0


    @pytest.mark.django_db
    def test_post_update_contributor_group_permission(db):
        client = Client()

        user = User.objects.create_user(
             username="testuser",
            email="test@example.com",
            password="pass123"
        )

        post_data = {
            "title": "Post Title",
            "content": "Post Content",
            "author": user.id
        }

        group = Group.objects.create(name="Contributor")
        client.login(username="testuser", password="pass123")

        content_type = ContentType.objects.get_for_model(Post)
        permission = Permission.objects.get(
            content_type=content_type,
            codename__icontains="add"
        )

        group.permissions.add(permission)
        user.groups.add(group)

    
        response = client.post(reverse("add_post"), post_data)

        updated_data = {
            "title": "Updated Post Title",
            "content": "Updated Post Content",
            "author": user.id
        }
        response = client.patch('edit_post//1', updated_data)

        assert response.status_code == 200



