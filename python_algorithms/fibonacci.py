
def fibonacci_rec(n: int) -> int:
    """A recursive function to calculate the nth fibonacci number.

    Args:
        n (int): The nth fibonacci number to calculate.

    Raises:
        ValueError: If n is not a positive integer.

    Returns:
        int: The nth fibonacci number.
    """

    if n < 0:
        raise ValueError("n must be a positive integer")
    elif n <= 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    """A function to calculate the nth fibonacci number.

    Args:
        n (int): The nth fibonacci number to calculate.

    Raises:
        ValueError: If n is not a positive integer.

    Returns:
        int: The nth fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be a positive integer")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
