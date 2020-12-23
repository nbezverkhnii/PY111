def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError()

    return fib_iterative(n - 1) + fib_iterative(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError()

    b =
    for i in range(n+1):



