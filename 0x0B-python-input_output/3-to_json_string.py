#!/usr/bin/python3
"""Defines a string_to_json function."""
import json


def to_json_string(my_obj):
    """Return the json representation of a string object."""
    return json.dumps(my_obj)
