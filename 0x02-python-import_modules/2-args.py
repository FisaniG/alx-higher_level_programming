#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv) - 1
    b = 1
    if a < 1:
        print("{:d} arguments.".format(a))
    elif a == 1:
        print("{:d}: argument:".format(a))
        print("{:d}: {:s}".format(a, argv[a]))
    else:
        print("{:d} arguments:".format(a))
        while(a > 0):
            print("{:d}: {:s}".format(b, argv[b]))
            b += 1
            a -= 1
