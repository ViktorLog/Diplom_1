import pytest

from test_values import BurgerSamples


class TestBurgerReceipt:
    @pytest.mark.parametrize("topping_count,receipt_lines", BurgerSamples.RECEIPT_CASES)
    def test_get_receipt_contains_components_and_total(self, empty_burger, bun_stub, topping_stubs, topping_count, receipt_lines):
        empty_burger.set_buns(bun_stub)
        empty_burger.ingredients = topping_stubs[:topping_count]

        expected_receipt = "\n".join(receipt_lines)
        assert empty_burger.get_receipt() == expected_receipt

