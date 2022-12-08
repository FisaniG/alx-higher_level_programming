#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = (len(argv) - 1)
    if size == 1:
        print(" 1 argument:")
    elif size < 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(size))
    for i in range(1, size + 1):
        print("{:d}:{:s}".format(i, argv[i]))
