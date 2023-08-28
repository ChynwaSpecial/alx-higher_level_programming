#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = my_list[:]
    for multiple, a in enumerate(my_list):
        if a % 2 == 0:
            boolist[multiple] = True
        else:
            boolist[multiple] = False
    return(boolist)
