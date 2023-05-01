import numpy as np


def calc_hx_arr(alf, fmp):
    if len(alf) != len(fmp):
        return -1
    return sum(map(lambda p: -p * (np.log2(p)), fmp))


def calc_hx_string(text):
    prob = [float(text.count(c)) / len(text) for c in dict.fromkeys(list(text))]
    return sum(map(lambda p: -p * (np.log2(p)), prob))


def char_to_binary(char):
    code_point = ord(char)
    binary = bin(code_point)[2:]
    binary = binary.zfill(8)
    return binary


def binary_to_char(binary):
    code_point = int(''.join(binary), 2)
    char = chr(code_point)
    return char
