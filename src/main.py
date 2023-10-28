from domain.entity.vending_machine import VendingMachine
from presentation.main_frame import MainFrame


def main():
    vending_machine = VendingMachine()

    main_frame = MainFrame(vending_machine)
    main_frame.launch()


if __name__ == "__main__":
    main()
