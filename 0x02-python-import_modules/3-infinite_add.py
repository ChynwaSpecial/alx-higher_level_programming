#!/usr/bin/python3
def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        j = 1
        add = 0
        while j <= n:
            add += int(argv[j])
            j += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
