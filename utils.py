import numpy as np


def calc_hx_arr(alf, fmp):
    if len(alf) != len(fmp):
        return -1
    return sum(map(lambda p: -p * (np.log2(p)), fmp))


def calc_hx_string(text):
    prob = [float(text.count(c)) / len(text) for c in dict.fromkeys(list(text))]
    return sum(map(lambda p: -p * (np.log2(p)), prob))
