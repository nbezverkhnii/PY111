from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    flag = True
    while flag:
        flag = False
        for i in range(len(container) - 1):
            if container[i] > container[i+1]:
                flag = True
                container[i], container[i+1] = container[i+1], container[i]

    return container

if __name__ == '__main__':
    arr = [95, 97, 99, 99, 28, 6, 53, 7, 73, 33, 41]
    print(arr)
    print(sort(arr))