#!/usr/bin/python3


def uniq_add(my_list=[]):
    if my_list is not None:
        new = set(my_list)
        z = list(new)
        sum = 0
        for i in z:
            sum += i
        return sum
    return None
