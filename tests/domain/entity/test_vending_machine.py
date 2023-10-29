from copy import deepcopy
from unittest import mock
from injector import Injector, InstanceProvider
import pytest
import sys, re

from pytest_mock import MockerFixture

sys.path.append(re.sub("VendingMachine\\\\tests.*", "VendingMachine\\\\src", __file__))

from configurator import configurator
from domain.entity.drink import Drink
from domain.entity.vending_machine import VendingMachine
from domain.value.money import Money
from domain.repository.drink_repository import DrinkRepository


@pytest.fixture(scope="function")
def mock_drink_repository(mocker: MockerFixture):
    repository = mocker.Mock()

    mocker.patch.object(repository, "add_drink")
    mocker.patch.object(repository, "find_all")

    with configurator.use(
        lambda binder: binder.bind(DrinkRepository, to=InstanceProvider(repository))
    ):
        yield repository


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
        self,
        money: Money,
        expected_entry_money: int,
        expected_ret: bool,
        mock_drink_repository: mock.Mock,
    ):
        """お金投入のテスト"""
        vending_machine = Injector(configurator).get(VendingMachine)

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
    def test_refund_money(
        self, money_list: list[Money], expected: int, mock_drink_repository: mock.Mock
    ):
        """釣銭取得のテスト"""
        vending_machine = Injector(configurator).get(VendingMachine)

        for m in money_list:
            vending_machine.entry_money(m)

        actual = vending_machine.refund_money()

        assert actual == expected

    def test_init(self, mock_drink_repository: mock.Mock):
        """コンストラクタのテスト"""
        add_drink_func: mock.Mock = mock_drink_repository.add_drink

        _ = Injector(configurator).get(VendingMachine)

        assert add_drink_func.call_count == 1

        _, unpack_kwargs = add_drink_func.call_args_list[0]
        assert unpack_kwargs.get("drink").name == "コーラ"
        assert unpack_kwargs.get("drink").price == 120
        assert unpack_kwargs.get("stock") == 5

    @pytest.mark.parametrize(
        ("store_data"),
        [
            ([]),
            ([(Drink("飲物1", 200), 10)]),
            ([(Drink("飲物2", 100), 10), (Drink("飲物3", 300), 5)]),
        ],
    )
    def test_get_drink_stock(self, mock_drink_repository: mock.Mock, store_data):
        """飲物一覧取得のテスト"""
        find_all_func: mock.Mock = mock_drink_repository.find_all
        find_all_func.return_value = deepcopy(store_data)

        vending_machine = Injector(configurator).get(VendingMachine)

        actual = vending_machine.get_drink_stock()

        assert actual == store_data
        find_all_func.assert_called_once()
