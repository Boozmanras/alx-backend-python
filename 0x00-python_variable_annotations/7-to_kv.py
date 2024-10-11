#!/usr/bin/env python3


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of an int or float.

    Args:
        k (str): The string to use as the first element of the tuple.
        v (Union[int, float]): The number to square for the second element.

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of v.
    """
    return (k, float(v ** 2))
