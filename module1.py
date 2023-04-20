import random

from utils import *
from ap1 import *
import pandas as pd
import numpy as np


def ex2a():
    ap1ex5d("a.txt")
    ap1ex5d("alice29.txt")
    ap1ex5d("cp.htm")
    ap1ex5d("lena.bmp")
    ap1ex5d("Person.java")
    ap1ex5d("progc.c")


# ex2a()


def ex2b(file_name):
    print('------------------------------------------------------------------------------------')
    print(file_name)
    chars = {}
    f = open(file_name, "r", encoding='iso-8859-1')
    while 1:
        c = f.read(1)
        if not c:
            break
        elif c in chars.keys():
            chars[c] += 1
        else:
            chars[c] = 1
    chars = dict(sorted(chars.items(), key=lambda x: x[0]))
    total_chars = sum(chars.values(), 0)
    char_prob = map(lambda x: (x / total_chars) * 100, chars.values())
    entropy = -1 * sum(map(lambda x: x / total_chars * np.log(x / total_chars), chars.values()))
    print('Entropy is: %f' % entropy)
    df = pd.DataFrame(data=list(zip(chars.keys(), chars.values(), char_prob)),
                      columns=['Char', 'n of Occurrences', '% of Occurrence'])
    print(df.to_string())


# ex2b("ListaPalavrasPT.txt")
# ex2b("ListaPalavrasEN.txt")

def ex3a(n, m, prob):
    gen = random.choices(m, prob, k=n)
    res = ''
    for c in gen:
        res += c
    return res


alpha = ['a', 'e', 'i', 'o', 'u']  # change this lines for
fmp = [0.25, 0.35, 0.05, 0.15, 0.2]  # different alphabets ands fmp


# print(ex3a(20, alpha, fmp))


def ex3b(size, times):
    hx = calc_hx_arr(alpha, fmp)
    print(f'Source Entropy: {hx}')
    for t in range(times):
        res = ex3a(size, alpha, fmp)
        hy = calc_hx_string(res)
        print(f'str: {res} -> entropy: {hy}')


# ex3b(10, 10)

def ex3c():
    abc = []
    for x in range(26):
        abc.append(chr(ord('a') + x))
    ABC = list(map(lambda y: y.upper(), abc))
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '$', '%', '&', '/', '€', '?']
    alphabet = abc + ABC + nums + symbols
    p = []
    for x in range(len(alphabet)):
        p.append(float(1 / len(alphabet)))
    while 1:
        res = ex3a(random.randint(8, 12), alphabet, p)
        if (
                any(substring in res for substring in abc) and
                any(substring in res for substring in ABC) and
                any(substring in res for substring in nums) and
                any(substring in res for substring in symbols)
        ):
            return res


# print(ex3c())

# make vernam cypher
def ex4a(plain_text, the_key):
    return list(map(lambda c: chr(ord(c[0]) ^ ord(c[1])), list(zip(plain_text, the_key))))


a = list('abcabcd')
b = list('3333333')


# print(ex4a(a, b))

def ex4b(file_name, constant):
    f = open(file_name, "r", encoding='iso-8859-1')
    buffer = []
    while 1:
        c = f.read(1)
        if not c:
            break
        else:
            buffer.append(c)
    key = []
    if constant is not None:
        for x in range(len(buffer)):
            key.append(constant)
    else:
        abc = []
        prob = []
        for x in range(255):
            abc.append(chr(ord('a') + x))
            prob.append(float(1 / 255))
        key = ex3a(len(buffer), abc, prob)
    print(ex4a(buffer, key))


# ex4b('alice29.txt', 'a')


def ex5a(seq, ber):
    alpha = ['0', '1']
    for_one = [float(ber), float(1 - ber)]
    for_zero = [float(1 - ber), float(ber)]
    final_seq = []
    for b in seq:
        if b == '1':
            final_seq.append(ex3a(1, alpha, for_one)[0])
        elif b == '0':
            final_seq.append(ex3a(1, alpha, for_zero)[0])
        else:
            return None
    return final_seq


print(ex5a('1010', float(0.25)))
