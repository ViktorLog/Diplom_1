import pytest

from test_values import BurgerSamples


class TestBurgerAssembly:
    def test_get_price_without_toppings(self, empty_burger, bun_stub):
        empty_burger.set_buns(bun_stub)

        assert empty_burger.get_price() == BurgerSamples.BREAD_PRICE * 2

    def test_set_buns_saves_selected_bun(self, empty_burger, bun_stub):
        empty_burger.set_buns(bun_stub)

        assert empty_burger.bun is bun_stub

    def test_add_ingredient_preserves_order(self, empty_burger, topping_stubs):
        for ingredient in topping_stubs:
            empty_burger.add_ingredient(ingredient)

        assert empty_burger.ingredients == topping_stubs

    @pytest.mark.parametrize('source_index,target_index', [(0, 1), (1, 0)])
    def test_move_ingredient_changes_position(self, empty_burger, topping_stubs, source_index, target_index):
        empty_burger.ingredients = topping_stubs.copy()

        empty_burger.move_ingredient(source_index, target_index)

        assert empty_burger.ingredients == [topping_stubs[1], topping_stubs[0]]

    @pytest.mark.parametrize('source_index', [0, 1])
    def test_remove_ingredient_by_position(self, empty_burger, topping_stubs, source_index):
        empty_burger.ingredients = topping_stubs.copy()

        empty_burger.remove_ingredient(source_index)

        assert empty_burger.ingredients == [topping_stubs[1 - source_index]]

