from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    start: int = 0
    end: int = len(arr) + 1
    # If arr is empty
    if not arr:
        return None

    def recursive(left: int, right: int):
        while left <= right:
            middle: int = left - (left - right)//2
            if arr[middle] == elem:
                # This loop implements left-side search
                while arr[middle-1] == elem:
                    middle -= 1
                return middle
            elif arr[middle] < elem:
                new_left = middle + 1
                return recursive(new_left, right)
            elif arr[middle] > elem:
                new_right = middle - 1
                return recursive(left, new_right)

    return recursive(start, end)
