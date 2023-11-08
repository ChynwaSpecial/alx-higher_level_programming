#!/usr/bin/python3
"""Defines a json_to_string function."""
import json


def from_json_string(my_str):
    """Return the json representation of the string object."""
    return json.loads(my_str)
