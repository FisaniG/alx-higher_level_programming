#!/usr/bin/python3
'''
task 4 json return string
'''


def to_json_string(my_obj):
    '''
    function to return json represantion of string
    '''
    import json

    return json.dumps(my_obj)
