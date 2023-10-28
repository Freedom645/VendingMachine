def convert_1d_to_2d(array: list, bp: int) -> list[list]:
    """1次元配列を指定したサイズで2次元配列に変換する

    Args:
        array (list): 対象の配列
        bp (int): ブレークポイント

    Returns:
        list[list]: ブレークポイントで区切った2次元配列
    """
    return [array[i : i + bp] for i in range(0, len(array), bp)]
