import sys, re

import pytest

sys.path.append(re.sub("VendingMachine\\\\tests.*", "VendingMachine\\\\src", __file__))

from domain.entity.drink import Drink


class TestDrink:
    def test_init(self):
        actual = Drink(name="飲物1", price=100)

        assert actual.name == "飲物1"
        assert actual.price == 100

    @pytest.mark.parametrize(
        ("name", "price", "expected"),
        [
            (None, 1, f"飲物名が指定されていません。:{None}"),
            ("", 2, "飲物名が指定されていません。:"),
            ("a", 0, "価格に不正な値が指定されました。:0"),
            (".", -1, "価格に不正な値が指定されました。:-1"),
        ],
    )
    def test_init_failed(self, name, price, expected):
        with pytest.raises(ValueError) as e:
            Drink(name=name, price=price)

        assert str(e.value) == expected
