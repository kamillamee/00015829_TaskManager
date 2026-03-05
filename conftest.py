"""
Pytest configuration and fixtures for Django tests.
"""
import os
import pytest
from django.contrib.auth import get_user_model

# Use SQLite for faster tests (no PostgreSQL needed in CI)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings_test')


@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create_user(username='testuser', password='testpass123', email='test@example.com')


@pytest.fixture
def auth_client(client, user):
    client.force_login(user)
    return client
