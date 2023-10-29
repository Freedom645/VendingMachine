from abc import abstractmethod, ABCMeta

from domain.entity.drink import Drink


class DrinkRepository(metaclass=ABCMeta):
    """飲物管理リポジトリのIF"""

    @abstractmethod
    def add_drink(self, drink: Drink, stock: int) -> None:
        """飲物を追加する

        Args:
            drink (Drink): 保存対象の飲物
            stock (int): 格納
        """
        raise NotImplementedError()

    @abstractmethod
    def find_all(self) -> list[tuple[Drink, int]]:
        """飲物在庫一覧を取得する

        Returns:
            list[tuple[Drink, int]]: 飲物と在庫数のリスト
        """
        raise NotImplementedError()
