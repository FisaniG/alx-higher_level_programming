#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    b = 1
    a = len(argv) - 1
    while (a > 0):
        d = int(argv[b])
        sum += d
        b += 1
        a -= 1

    print("{:d}".format(sum))
