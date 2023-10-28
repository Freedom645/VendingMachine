import pytest
import sys, re

sys.path.append(re.sub("VendingMachine\\\\tests.*", "VendingMachine\\\\src", __file__))

from domain.entity.vending_machine import VendingMachine
from domain.value.money import Money


class TestVendingMachine:
    @pytest.mark.parametrize(
        ("money", "expected_entry_money", "expected_ret"),
        [
            (Money.M_1, 0, False),
            (Money.M_5, 0, False),
            (Money.M_10, 10, True),
            (Money.M_50, 50, True),
            (Money.M_100, 100, True),
            (Money.M_500, 500, True),
            (Money.M_1000, 1000, True),
            (Money.M_2000, 0, False),
            (Money.M_5000, 0, False),
            (Money.M_10000, 0, False),
        ],
    )
    def test_entry_money(
        self, money: Money, expected_entry_money: int, expected_ret: bool
    ):
        vending_machine = VendingMachine()

        ret = vending_machine.entry_money(money)

        assert vending_machine.get_entry_money() == expected_entry_money
        assert ret == expected_ret

    @pytest.mark.parametrize(
        ("money_list", "expected"),
        [
            ([Money.M_1, Money.M_5], 0),
            ([Money.M_1, Money.M_10], 10),
            ([Money.M_50, Money.M_100], 150),
            ([Money.M_500, Money.M_1000], 1500),
            ([Money.M_500, Money.M_5, Money.M_1000], 1500),
        ],
    )
    def test_refund_money(self, money_list: list[Money], expected: int):
        vending_machine = VendingMachine()

        for m in money_list:
            vending_machine.entry_money(m)

        actual = vending_machine.refund_money()

        assert actual == expected
