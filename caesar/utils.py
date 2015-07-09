#!/usr/bin/python3


def input_for_python_2_3():
    try:
        return raw_input
    except:
        return input

