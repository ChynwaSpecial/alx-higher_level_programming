#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    current_list = my_list[:]
    if 0 <= idx < len(my_list):
        current_list[idx] = element
        return(current_list)
    return(my_list)
