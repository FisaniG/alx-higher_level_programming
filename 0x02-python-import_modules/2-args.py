#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = (len(argv) - 1)
    if size == 1:
        print("{0} argument:".format(size))
    elif size < 1:
        print("{0} arguments.".format(size))
    else:
        print("{0} arguments:".format(size))
    for i in range(1, size + 1):
        print("{0}: {1}".format(i, argv[i]))
