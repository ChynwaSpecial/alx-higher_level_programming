#!/usr/bin/python3
def complex_delete(my_dictionary, value):
    tmp = my_dictionary.copy()
    for i, j in tmp.items():
        if value == j:
            my_dictionary.pop(i)
    return my_dictionary
