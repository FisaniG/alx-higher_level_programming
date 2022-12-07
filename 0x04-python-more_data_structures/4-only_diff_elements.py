#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    if set_1 and set_2 is None:
        return None
    new = []
    for i in set_1:
        if i in set_2:
            pass
        else:
            new.append(i)
    for i in set_2:
        if i in set_1:
            pass
        else:
            new.append(i)
    return set(new)
