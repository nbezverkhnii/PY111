"""
Taylor series
"""
from typing import Union
from math import factorial
from itertools import count

DELTA = 0.0001

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    ex_sum = 0
    for n in count():
        a = pow(x, n)
        b = factorial(n)
        ex_sum += a / b

        if abs(a / b) <= DELTA:
            return ex_sum



def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sin_sum = 0
    for n in count(1):
        a = pow(x, 2 * n - 1)
        b = factorial(2 * n - 1)
        res = pow(-1, n + 1) * a / b
        sin_sum += res

        if abs(res) <= DELTA:
            return sin_sum
