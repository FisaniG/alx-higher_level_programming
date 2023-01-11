#!/usr/bin/python3


'''
task 0, read and print file
'''


def read_file(filename=""):
    '''
    function to read file
    '''
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
