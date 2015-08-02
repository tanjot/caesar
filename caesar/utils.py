#!/usr/bin/python3


def input_for_python_2_3():
    try:
        return raw_input
    except:
        return input


def read_dict_from_file(filename):
    data_in_dict = {}
    with open(filename, 'r') as fhan:
        server_ip = fhan.readline().strip()
        data_in_dict[server_ip] = fhan.readline().strip()


def write_dict_to_file(filename, key, value):
    with open(filename, 'a') as fhan:
        fhan.write(key+'\n')
        fhan.write(value+'\n')

