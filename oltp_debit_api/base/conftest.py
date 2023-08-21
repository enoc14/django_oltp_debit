import pytest
from rest_framework.test import APIClient
from .models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def user_payload():
    return {
        'name': 'John Doe',
        'age': 38,
        'city': 'New York'
    }


@pytest.fixture
def create_user():
    payload = {
        'name': 'John Doe',
        'age': 38,
        'city': 'New York'
    }
    record = User.objects.create(**payload)
    return record
