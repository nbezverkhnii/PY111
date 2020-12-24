from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, magic: int = 0) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    start = 0
    end = len(arr) + 1

    if len(arr) == 0:
        return None
    elif len(arr) == 1 and arr[0] != elem:
        return None
    elif len(arr) == 1 and arr[0] == elem:
        return 0 + magic

    while start <= end:
        middle = int((start + end)/2)
        if arr[middle] < elem:
            magic += middle
            binary_search(elem, arr[middle+1:end], magic)
        elif arr[middle] > elem:
            magic -= middle
            binary_search(elem, arr[start:middle-1], magic)

