from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container

    pivot = container[0]
    less = [i for i in container[1:] if i <= pivot]
    greather = [i for i in container[1:] if i >= pivot]

    return sort(less) + [pivot] + sort(greather)


if __name__ == '__main__':
    arr = [52, 12, 3, 89, 43, 28, 66, 1, 28, 7, 85, 74, 19, 35, 2]
    print(arr)
    print(sort(arr))