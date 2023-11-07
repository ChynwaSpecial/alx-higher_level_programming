#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a baseclass .

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the object type.
    Returns:
        If obj is an instance or inherited instance of a_class then True.
        Otherwise  False.
    """
    if isinstance(obj, a_class):
        return True
    return False
