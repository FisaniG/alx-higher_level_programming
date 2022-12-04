#!/usr/bin/python3


def multiple_returns(sentence):
    strlen = len(sentence)
    if strlen == 0:
        return strlen, "None"
    else:
        return strlen, sentence[0]
