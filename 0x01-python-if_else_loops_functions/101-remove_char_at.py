#!/usr/bin/python3
def remove_char_at(str, n):
    new_char = ""
    j = 0
    for c in str:
        if j != n:
            new_char += c
        j += 1
    return new_char
