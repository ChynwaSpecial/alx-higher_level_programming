#!/usr/bin/python3
def print_sorted_dictionary(my_dictionary):
    for k in sorted(my_dictionary.keys()):
        print("{}: {}".format(k, my_dictionary[k]))
