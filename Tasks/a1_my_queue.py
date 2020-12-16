"""
My little Queue
"""
from typing import Any

my_queue = [] # конец слева

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    my_queue.insert(0, elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    return my_queue.pop() if my_queue else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return None if ind >= len(my_queue) else my_queue[-1 - ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    my_queue.clear()
    return None

if __name__ == '__main__':
    enqueue(1)
    print(my_queue)