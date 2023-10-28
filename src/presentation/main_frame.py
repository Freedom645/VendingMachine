from enum import Enum
import PySimpleGUI as sg
from PySimpleGUI import Element

from domain.entity.vending_machine import VendingMachine
from domain.value.money import Money


class ElementKey(Enum):
    EntryAmountText = "entry-amount-text"
    MoneyButton = "money-button"
    RefundButton = "refund-button"
    ChangeText = "change-text"


class MainFrame:
    def __init__(self, vending_machine: VendingMachine) -> None:
        self.__vending_machine = vending_machine

    def __setup_layout(self) -> list[list[Element]]:
        layout = [
            [sg.Text("投入金額: ¥0", key=ElementKey.EntryAmountText)],
            self.__generate_money_buttons(),
            [sg.Button(button_text="払戻し", key=ElementKey.RefundButton)],
            [sg.Text("釣銭: ¥0", key=ElementKey.ChangeText)],
        ]

        return layout

    def __generate_money_buttons(self) -> list:
        money_list = VendingMachine.usable_money_list()
        return [
            sg.Button(
                f"{money.to_int()}円",
                key=f"{ElementKey.MoneyButton.value}-{money.to_int()}",
            )
            for money in money_list
        ]

    def launch(self) -> None:
        sg.theme("DarkAmber")
        layout = self.__setup_layout()
        self.window = sg.Window("自動販売機", layout)

        while True:
            event, _ = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event.__str__().startswith(ElementKey.MoneyButton.value):
                self.__entry_money(event)
            elif event == ElementKey.RefundButton:
                self.__refund()

        self.window.close()

    def __entry_money(self, key: str):
        """お金投入イベント"""
        money = Money.from_int(int(key.split("-")[-1]))
        self.__vending_machine.entry_money(money)

        entry_amount = self.__vending_machine.get_entry_money()
        entry_amount_text: sg.Text = self.window[ElementKey.EntryAmountText]
        entry_amount_text.update(value=f"投入金額: ¥{entry_amount}")

    def __refund(self):
        """払戻しイベント"""
        change = self.__vending_machine.refund_money()

        change_text: sg.Text = self.window[ElementKey.ChangeText]
        change_text.update(value=f"釣銭: ¥{change}")

        entry_amount = self.__vending_machine.get_entry_money()
        entry_amount_text: sg.Text = self.window[ElementKey.EntryAmountText]
        entry_amount_text.update(value=f"投入金額: ¥{entry_amount}")
