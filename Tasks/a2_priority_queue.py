"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

# Так как мы заранее знаем количество приоритетов,
# то может попробовать реалзовать очередь с приритетом
# имеющую теоретическую сложность операций enqueue и dequeue О(1)
# Однако, я не додумался как сделать dequeue О(1)
my_prior_queue = [[] for _ in range(11)]

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue
    :param elem: element to be added
    :return: Nothing
    """
    my_prior_queue[priority].append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.
    :return: dequeued element
    """
    result = None
    for queue in my_prior_queue:
        # Если не пуст
        if queue:
            result = queue.pop(0)
            break
    return result


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it
    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return my_prior_queue[priority][ind] if my_prior_queue[priority][ind] else None


def clear() -> None:
    """
    Clear my queue
    :return: None
    """
    for queue in my_prior_queue:
        queue.clear()
    return None

if __name__ == '__main__':
    enqueue(3)
    enqueue(5)
    enqueue(7)
    print(my_prior_queue)
    print(peek())
    print(peek(1))
    print(peek())
