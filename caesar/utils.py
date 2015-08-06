#!/usr/bin/python3


def input_for_python_2_3():
    try:
        return raw_input
    except:
        return input


def read_dict_from_file(filename):
    data_in_dict = {}
    try:
        with open(filename, 'r') as fhan:
            server_ip = fhan.readline().strip()
            data_in_dict[server_ip] = fhan.readline().strip()
    except FileNotFoundError:
        self.logger.print_log(VERBOSITY_LEVELS['error'], 'Configuration file does not exist')

    return data_in_dict


def write_dict_to_file(filename, key, value):
    with open(filename, 'ab') as fhan:
        fhan.write(bytes(key+'\n', 'UTF-8'))
        fhan.write(value)
        fhan.write(bytes('\n'+'UTF-8'))

