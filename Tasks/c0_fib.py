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

    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i-2] + fib_list[i-1])

    return fib_list[-1]


