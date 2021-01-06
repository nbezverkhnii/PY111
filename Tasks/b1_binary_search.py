from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    start = 0
    finish = len(arr) - 1

    while start <= finish:
        # Например в Java возможно переполнение типа int при start+finish, поэтому по-другому будем считать
        middle = start - int((start-finish)/2)
        if arr[middle] == elem:
            return middle
        elif arr[middle] <= elem:
            start = middle + 1
        else:
            finish = middle - 1

