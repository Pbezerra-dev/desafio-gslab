import pytest
import json

from django.urls import reverse
from decimal import Decimal
from collections import OrderedDict
from products.core.models import Product
from model_bakery import baker

from products.django_assertions import assert_equal


# SUCCESS
@pytest.fixture
def product(db):
    return baker.make(
        Product, id=1, name='Name', description='Descricao', price=Decimal('200.00')
    )


@pytest.fixture
def resp_create_prod(client_with_logged_in_user, client):
    data = {'name': 'Name', 'description': 'Descricao', 'price': Decimal('100.00')}
    return client.post(reverse('products_api:products'), data=data)


@pytest.fixture
def resp_list_prods(client_with_logged_in_user, client, product):
    return client.get(reverse('products_api:products'))


@pytest.fixture
def resp_list_prod_by_id(client_with_logged_in_user, client, product):
    return client.get(reverse('products_api:product', kwargs={'pk': 1}))


@pytest.fixture
def resp_update_prod(client_with_logged_in_user, client, product):
    data = json.dumps(
        {
            'name': 'Name',
            'description': 'Descricao',
            'price': 250.00,
        }
    )
    return client.put(
        reverse('products_api:update', kwargs={'pk': 1}),
        data=data,
        content_type='application/json',
    )


@pytest.fixture
def resp_delete_prod(client_with_logged_in_user, client, product):
    return client.delete(reverse('products_api:delete', kwargs={'pk': 1}))


def test_create_prod(resp_create_prod):
    data = {'id': 1, 'name': 'Name', 'description': 'Descricao', 'price': '100.00'}
    assert resp_create_prod.status_code == 201
    assert_equal(resp_create_prod.data, data)


def test_list_prods(resp_list_prods):
    data = [
        OrderedDict(
            [
                ('id', 1),
                ('name', 'Name'),
                ('description', 'Descricao'),
                ('price', '200.00'),
            ]
        ),
    ]

    assert resp_list_prods.status_code == 200
    assert_equal(resp_list_prods.data, data)


def test_list_prod_by_id(resp_list_prod_by_id):
    data = {'id': 1, 'name': 'Name', 'description': 'Descricao', 'price': '200.00'}
    assert resp_list_prod_by_id.status_code == 200
    assert_equal(resp_list_prod_by_id.data, data)


def test_update_prod(resp_update_prod):
    data = {'id': 1, 'name': 'Name', 'description': 'Descricao', 'price': '250.00'}
    assert resp_update_prod.status_code == 200
    assert_equal(resp_update_prod.data, data)


def test_delete_prod(resp_delete_prod):
    assert resp_delete_prod.status_code == 204


# ERRORS


@pytest.fixture
def resp_create_prod_fail(client_with_logged_in_user, client):
    data = {'name': 'Nome', 'description': 'Descricao', 'price': Decimal('-100.00')}
    return client.post(reverse('products_api:products'), data=data)


@pytest.fixture
def resp_list_prod_by_id_fail(client_with_logged_in_user, client, product):
    return client.get(reverse('products_api:product', kwargs={'pk': 5}))


@pytest.fixture
def resp_update_prod_fail(client_with_logged_in_user, client, product):
    data = {
        'price': Decimal('250.00'),
    }
    return client.put(reverse('products_api:update', kwargs={'pk': 5}), json=data)


@pytest.fixture
def resp_delete_prod_fail(client_with_logged_in_user, client, product):
    return client.delete(reverse('products_api:delete', kwargs={'pk': 5}))


def test_create_prod_fail(resp_create_prod_fail):
    data = {'price': ['Certifque-se de que este valor seja maior ou igual a 1.']}
    assert resp_create_prod_fail.status_code == 400
    assert_equal(json.dumps(resp_create_prod_fail.data), json.dumps(data))


def test_list_prod_by_id_fail(resp_list_prod_by_id_fail):
    data = {'detail': 'Produto não encontrado'}
    assert resp_list_prod_by_id_fail.status_code == 404
    assert_equal(resp_list_prod_by_id_fail.data, data)


def test_update_prod_fail(resp_update_prod_fail):
    data = {'detail': 'Produto não encontrado'}
    assert resp_update_prod_fail.status_code == 404
    assert_equal(resp_update_prod_fail.data, data)


def test_delete_prod_fail(resp_delete_prod_fail):
    data = {'detail': 'Produto não encontrado'}
    assert resp_delete_prod_fail.status_code == 404
    assert_equal(resp_delete_prod_fail.data, data)
