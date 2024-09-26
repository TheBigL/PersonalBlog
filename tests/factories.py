import factory
from faker import Faker

class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.text(20)
    email = fake.email()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = fake.text(150)
    author = factory.SubFactory(MemberFactory)
    content = fake.text()