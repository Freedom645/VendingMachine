from injector import Injector
from configurator import configurator

from domain.repository.drink_repository import DrinkRepository
from infrastructure.repository.drink_repository_impl import DrinkRepositoryImpl
from presentation.main_frame import MainFrame


def main():
    configurator.add(
        lambda binder: binder.bind(DrinkRepository, to=DrinkRepositoryImpl)
    )

    injector = Injector(configurator)

    main_frame: MainFrame = injector.get(MainFrame)
    main_frame.launch()


if __name__ == "__main__":
    main()
