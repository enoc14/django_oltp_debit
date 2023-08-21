import pytest
from rest_framework import status

from .models import User


@pytest.mark.django_db
def test_create_user(api_client, user_payload):
    response = api_client.post('/api/users/', user_payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_get_users(api_client, create_user):
    response = api_client.get('/api/users/')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    user_data = dict(response.data[0])
    assert user_data['name'] == create_user.name
    assert user_data['age'] == create_user.age
    assert user_data['city'] == create_user.city


@pytest.mark.django_db
def test_update_user(api_client, create_user):
    user_id = create_user.id
    payload_to_update = {
        'name': 'Michael Scott',
        'age': 55,
        'city': 'Las Vegas'
    }

    response = api_client.patch(f'/api/users/{user_id}', payload_to_update, format='json')
    assert response.status_code == 200
    assert response.data['name'] != create_user.name
    assert response.data['age'] != create_user.name
    assert response.data['city'] != create_user.name


@pytest.mark.django_db
def test_delete_user(api_client, create_user):
    user_id = create_user.id

    response = api_client.delete(f'/api/users/{user_id}')
    assert response.status_code == 204
