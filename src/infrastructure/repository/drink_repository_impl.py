from domain.entity.drink import Drink
from domain.repository.drink_repository import DrinkRepository


class DrinkRepositoryImpl(DrinkRepository):
    def __init__(self) -> None:
        super().__init__()
        self.__db: dict[str, tuple[Drink, int]] = {}

    def add_drink(self, drink: Drink, stock: int) -> None:
        record = self.__db.get(drink.name, (drink, 0))
        record = (drink, record[1] + stock)

        self.__db.update(zip(drink.name, record))

    def find_all(self) -> list[tuple[Drink, int]]:
        return list(self.__db.items())
