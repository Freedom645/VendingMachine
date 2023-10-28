import pytest
import sys, re

sys.path.append(re.sub("VendingMachine\\\\tests.*", "VendingMachine\\\\src", __file__))

from domain.value.money import Money


class TestMoney:
    @pytest.mark.parametrize(
        ("money", "expected"),
        [
            (Money.M_1, 1),
            (Money.M_5, 5),
            (Money.M_10, 10),
            (Money.M_50, 50),
            (Money.M_100, 100),
            (Money.M_500, 500),
            (Money.M_1000, 1000),
            (Money.M_2000, 2000),
            (Money.M_5000, 5000),
            (Money.M_10000, 10000),
        ],
    )
    def test_to_int(self, money: Money, expected: int):
        assert money.to_int() == expected

    @pytest.mark.parametrize(
        ("expected", "value"),
        [
            (Money.M_1, 1),
            (Money.M_5, 5),
            (Money.M_10, 10),
            (Money.M_50, 50),
            (Money.M_100, 100),
            (Money.M_500, 500),
            (Money.M_1000, 1000),
            (Money.M_2000, 2000),
            (Money.M_5000, 5000),
            (Money.M_10000, 10000),
        ],
    )
    def test_from_int(self, value: int, expected: Money):
        assert Money.from_int(value) == expected

    def test_from_int_failed(self):
        value = 2
        with pytest.raises(ValueError) as e:
            Money.from_int(value)

        assert str(e.value) == f"{value}は未定義の値です"
