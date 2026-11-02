from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from test_values import BurgerSamples


@pytest.fixture
def empty_burger():
    return Burger()


@pytest.fixture
def bun_stub():
    bread = Mock()
    bread.get_name.return_value = BurgerSamples.BREAD_NAME
    bread.get_price.return_value = BurgerSamples.BREAD_PRICE
    return bread


@pytest.fixture
def topping_stubs():
    sauce_stub = Mock()
    sauce_stub.get_name.return_value = BurgerSamples.SAUCE_NAME
    sauce_stub.get_type.return_value = BurgerSamples.SAUCE_KIND
    sauce_stub.get_price.return_value = BurgerSamples.SAUCE_PRICE
    filling_stub = Mock()
    filling_stub.get_name.return_value = BurgerSamples.FILLING_NAME
    filling_stub.get_type.return_value = BurgerSamples.FILLING_KIND
    filling_stub.get_price.return_value = BurgerSamples.FILLING_PRICE
    return [sauce_stub, filling_stub]
