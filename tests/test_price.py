import pytest

from test_values import BurgerSamples


class TestBurgerPrice:
    @pytest.mark.parametrize('topping_count,expected_result', BurgerSamples.PRICE_CASES)
    def test_price_includes_bun_pair_and_toppings(self, empty_burger, bun_stub, topping_stubs, topping_count, expected_result):
        empty_burger.set_buns(bun_stub)
        empty_burger.ingredients = topping_stubs[:topping_count]

        assert empty_burger.get_price() == expected_result

