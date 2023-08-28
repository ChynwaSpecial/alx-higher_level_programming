#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    args = sys.argv
    length = len(args) - 1

    if length > 1:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, args[i]))

    elif length == 0:
        print("{} arguments.".format(length))

    else:
        print("{} argument:".format(length))
        print("{}: {}".format(length, args[1]))
