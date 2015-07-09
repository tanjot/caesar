#!/usr/bin/python3


def input_for_python_2_3(self):
    try:
        return raw_input
    except:
        print('In except')
        return input

