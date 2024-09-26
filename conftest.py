import pytest

from pytest_factoryboy import register
from tests.factories import MemberFactory, PostFactory

register(MemberFactory) 
register(PostFactory)