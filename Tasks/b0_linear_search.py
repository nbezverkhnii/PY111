"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    if arr:
        min_element: int = arr[0]
        for item in arr:
            if item < min_element:
                min_element = item
        return arr.index(min_element)
    else:
        print('Sequence is empty')
        return None

if __name__ == '__main__':
    print(min_search([]))
