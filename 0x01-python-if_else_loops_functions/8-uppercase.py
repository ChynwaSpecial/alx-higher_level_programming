#!/usr/bin/python3
def uppercase(string):
    string_new = ""
    for c in string:
        if 'a' <= c <= 'z':
            string_new += chr(ord(c) - 32)
        else:
            string_new+= c
    print("{:s}".format(string_new))
