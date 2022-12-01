#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    a = dir(hidden_4)
    b = '__'
    for i in a:
        if b not in i:
            print(i)
