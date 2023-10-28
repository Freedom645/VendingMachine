import PySimpleGUI as sg

from domain.entity.drink import Drink


class DrinkFrame:
    def __init__(self, drink: Drink, stock: int) -> None:
        self.__layout = [
            [
                sg.Text(
                    f"{drink.name}\n¥{drink.price}", size=[6, 3], justification="center"
                )
            ],
            [sg.Text(f"残: {stock}本", size=[6, 2], justification="center")],
        ]

    def build(self) -> sg.Frame:
        return sg.Frame(title="", layout=self.__layout)
