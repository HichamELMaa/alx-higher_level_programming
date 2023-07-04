#!/usr/bin/python3
def add_integer(a, b=98):
    """Return the integer addition of a and b.

    If either a or b is a float, they are typecasted to ints before addition.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is neither an integer nor a float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
