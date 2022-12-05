#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    opsign = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op not in opsign:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("{} {} {} = {}".format(a, op, b, opsign[op](a, b)))
