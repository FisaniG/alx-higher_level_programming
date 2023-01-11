#!/usr/bin/python3


'''
task 1 write to file
'''


def write_file(filename="", text=""):
    '''
    write to file and return the number of written characters
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
