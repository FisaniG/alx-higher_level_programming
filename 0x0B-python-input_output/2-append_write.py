#!/usr/bin/python3


'''
task 3 append to file
'''


def append_write(filename="", text=""):
    '''
    function to append text to the end of file
    '''
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
