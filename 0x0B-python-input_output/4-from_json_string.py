#!/usr/bin/python3
'''
task 5 deserialize
'''


def from_json_string(my_str):
    '''
    function to deselialize from json
    '''
    import json

    return json.loads(my_str)
