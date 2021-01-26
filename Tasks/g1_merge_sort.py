from typing import List

def merge(left_sublist: List[int], right_sublist: List[int],) -> List[int]:
    """
    Merged left_sublist and right_sublist with Merge Sot Rules

    :param left_sublist: left subconteiner
    :param right_sublist: right subconteiner
    :return: merged left_sublist and right_sublist
    """
    merged: List[int] = []
    left_index: int = 0
    right_index: int = 0

    while left_index < len(left_sublist) and right_index < len(right_sublist):
        if left_sublist[left_index] <= right_sublist[right_index]:
            merged.append(left_sublist[left_index])
            left_index += 1
        elif left_sublist[left_index] >= right_sublist[right_index]:
            merged.append(right_sublist[right_index])
            right_index += 1

    merged.extend(right_sublist[right_index:])
    merged.extend(left_sublist[left_index:])

    return merged


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container

    middle: int = len(container) // 2
    left_subconteiner: List[int] = sort(container[:middle])
    right_subconteiner: List[int] = sort(container[middle:])

    return merge(left_subconteiner, right_subconteiner)


if __name__ == '__main__':
    arr = [54, 23, 867, 1, 345, 7, 0, 435, 84, 35, 7, 0, 33, 9]
    print(arr)
    print(sort(arr))
