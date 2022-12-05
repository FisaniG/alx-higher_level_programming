#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv) - 1
    b = 1
    if a < 2:
        if a == 0:
            print("{:d} arguments.".format(a))
        else:
            print("{:d}: argument:".format(a))
            print("{:d}: {}".format(a, argv[a]))
    else:
        print("{:d} arguments:".format(a))
        for i in range(a):
            print("{:d}: {:s}".format((i + 1), argv[i + 1]))
