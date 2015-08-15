#!/usr/bin/python3

import base64
import configparser

def input_for_python_2_3():
    try:
        return raw_input
    except:
        return input


def read_dict_from_file(filename):
    data_in_dict = {}
    try:
        fhan = open(filename, 'r')

        line = fhan.readline().strip()
        while line:
            server_ip = line
            data_in_dict[server_ip] = fhan.readline().strip()
            line = fhan.readline().strip()

    except FileNotFoundError:
        #self.logger.print_log(VERBOSITY_LEVELS['error'], 'Configuration file does not exist')
        print("FileNotFoundError")

    return data_in_dict

def encode_data(data):
    return base64.b64encode((data).encode('UTF-8'))

def decode_data(encoded_data):
    return (base64.b64decode(encoded_data).decode('UTF-8'))

def append_key_value_to_file(filename, key, value):
    fhan = open(filename, 'ab')
    add_key_value_to_file(fhan, key, value)
    fhan.close()


def add_key_value_to_file(fhan, key, value):
    fhan.write(bytes(key+'\n', 'UTF-8'))
    if type(value) is bytes:
        fhan.write(value)
    else:
        fhan.write(bytes(value, 'UTF-8'))
    fhan.write(bytes('\n','UTF-8'))


def write_dict_to_file(filename, dict_to_fill):
    fhan = open(filename, 'wb')
    for key in dict_to_fill.keys():
        add_key_value_to_file(fhan, key, dict_to_fill[key])
    fhan.close()
