from enum import Enum


class Money(Enum):
    """お金種別クラス"""

    M_1 = 1
    M_5 = 5
    M_10 = 10
    M_50 = 50
    M_100 = 100
    M_500 = 500
    M_1000 = 1000
    M_2000 = 2000
    M_5000 = 5000
    M_10000 = 10000

    def to_int(self) -> int:
        return self.value

    @staticmethod
    def from_int(value: int):
        for e in Money:
            if e.value == value:
                return e
        raise ValueError(f"{value} is not Money")
