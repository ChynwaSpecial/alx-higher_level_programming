#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    a = my_list[0]
    for j in my_list:
        if j > a:
            a = j
    return (a)
