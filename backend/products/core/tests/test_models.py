import pytest

from model_bakery import baker
from products.core.models import Product

from products.django_assertions import assert_equal


@pytest.fixture
def product(db):
    product = baker.make(Product)

    return product


def test_person_rep(product):
    assert_equal(str(product), product.name)
