from typing import Callable, TypeVar
from injector import Binder, Injector

from domain.entity.vending_machine import VendingMachine
from domain.repository.drink_repository import DrinkRepository
from infrastructure.repository.drink_repository_impl import DrinkRepositoryImpl
from presentation.main_frame import MainFrame


class DependencyBuilder:
    def __init__(self):
        self._injector = Injector(self.__class__.configure)

    @classmethod
    def configure(self, binder: Binder) -> None:
        binder.bind(DrinkRepository, to=DrinkRepositoryImpl)

    def __getitem__(self, klass: type[TypeVar("T")]) -> Callable:
        return lambda: self._injector.get(klass)


def main():
    dependency = DependencyBuilder()

    vending_machine = VendingMachine(dependency[DrinkRepository]())

    main_frame = MainFrame(vending_machine)
    main_frame.launch()


if __name__ == "__main__":
    main()
