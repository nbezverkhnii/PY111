"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

# Так как мы заранее знаем количество приоритетов,
# то может попробовать реалзовать очередь с приритетом
# имеющую теоретическую сложность операций enqueue и dequeue О(1)
# Однако, я не додумался как сделать dequeue О(1)
my_priority_queue = [[] for _ in range(11)]

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue
    :param elem: element to be added
    :return: Nothing
    """
    my_priority_queue[priority].append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.
    :return: dequeued element
    """
    result = None
    for priority in my_priority_queue:
        # Если не пуст
        if priority:
            result = priority.pop(0)
            break
    return result


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element by index and by priority in the queue without dequeuing it
    :param ind: index of element (count from the beginning)
    :param priority: index of priority
    :return: peeked element
    """
    # Так как (преднаписаная) функция принимает два аргумента, то предполагается, что можно смотреть не только в
    # очередь c наивысшим приоритетом, и не только на первый элемент. Иначе стоило бы вынести один из
    # аргументов в константы или просто убрать его из аргументов.
    # Такая реализация, не противоречит принципу работы Priority Queue, а просто немного раширяет функционал
    try:
        return my_priority_queue[priority][ind] if my_priority_queue[priority][ind] else None
    except IndexError:
        print(f'There is no element with index {ind} and priority {priority}')
        return None


def clear() -> None:
    """
    Clear my queue
    It's clear the queue priority by priority
    :return: None
    """
    for queue in my_priority_queue:
        queue.clear()
    return None

if __name__ == '__main__':
    enqueue(3)
    enqueue(5)
    enqueue(7)
    print(my_priority_queue)
    print(peek())
    print(peek(1))
    print(peek(3))
    print(peek(1,1))
    print(peek())
