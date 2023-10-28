from dataclasses import dataclass


@dataclass
class Drink:
    """飲物クラス"""

    def __init__(self, name: str, price: int) -> None:
        """コンストラクタ

        Args:
            name (str): 飲物の名称
            price (int): 飲物の価格

        Raises:
            ValueError: 飲物の名称が指定されていない場合
            ValueError: 飲物価格に自然数でない値が指定された場合
        """
        if name is None or name == "":
            raise ValueError(f"飲物名が指定されていません。:{name}")
        if price is None or not isinstance(price, int) or price <= 0:
            raise ValueError(f"価格に不正な値が指定されました。:{price}")

        self.name = name
        self.price = price
