#!/usr/bin/python3
"""Defines a json creating_object function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a json file."""
    with open(filename) as f:
        return json.load(f)
