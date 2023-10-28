from domain.entity.drink import Drink
from domain.repository.drink_repository import DrinkRepository
from domain.value.money import Money


class VendingMachine:
    """自動販売機クラス

    Attributes:
        entry_money (int): 投入金額の総計
    """

    def __init__(self, drink_repository: DrinkRepository) -> None:
        self.__entry_money = 0

        self.__drink_repository = drink_repository
        self.__drink_repository.add_drink(drink=Drink(name="コーラ", price=120), stock=5)

    def entry_money(self, money: Money) -> bool:
        """お金を投入する

        Args:
            money (Money): 投入するお金の種類

        Returns:
            bool: 投入に成功した場合はTrueを返す
        """
        if money not in VendingMachine.usable_money_list():
            print(f"{money} is unusable.")
            return False

        self.__entry_money += money.value
        return True

    def refund_money(self) -> int:
        """払い戻しをする

        Returns:
            int: 払い戻し金額
        """
        refundment = self.__entry_money
        self.__entry_money = 0
        return refundment

    def get_entry_money(self) -> int:
        """投入金額を取得する

        Returns:
            int: 投入金額
        """
        return self.__entry_money

    @staticmethod
    def usable_money_list() -> list[Money]:
        """自動販売機に利用可能なお金の種別リストを返す

        Returns:
            list[Money]: 利用可能なお金の種別リスト
        """
        return [Money.M_10, Money.M_50, Money.M_100, Money.M_500, Money.M_1000]
