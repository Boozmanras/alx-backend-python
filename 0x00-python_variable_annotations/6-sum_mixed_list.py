#!/usr/bin/env python3


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of
       integers and floats to sum.

    Returns:
        float: The sum of all numbers in the input list.
    """
    return float(sum(mxd_lst))
