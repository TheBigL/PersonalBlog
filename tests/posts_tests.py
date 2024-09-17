import pytest
from django.contrib.auth import get_user_model
from posts.models import Post

# Create your tests here.
User = get_user_model()

#Fixture

@pytest.fixture()
def contributor(db):
    contributor = User.objects.create_user('contributor@test.com', 'contributor')
    contributor.is_contributor = True
    yield contributor

@pytest.fixture()
def reg(db):
    reg = User.objects.create_user('reg@test.com', 'Regular')
    yield reg

@pytest.mark.django_db
def reg_cannot_post(db):
    new_post = Post.objects.create()
    

