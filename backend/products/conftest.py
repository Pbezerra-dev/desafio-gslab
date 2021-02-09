import pytest

from model_bakery import baker
from products.core.models import Product
from decimal import Decimal


@pytest.fixture
def user_logged(db, django_user_model):
    user_model = baker.make(django_user_model, first_name='user')

    return user_model


@pytest.fixture
def client_with_logged_in_user(user_logged, client):
    client.force_login(user_logged)
    return client


@pytest.fixture
def product(db):
    return baker.make(
        Product, name='Name', description='Descricao', price=Decimal('200.00')
    )
