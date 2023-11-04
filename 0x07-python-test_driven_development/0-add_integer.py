#!/usr/bin/python3

"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to integer before addition is performed.
    Raises:
        TypeError: If neither a nor b is integer and float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a + b)
