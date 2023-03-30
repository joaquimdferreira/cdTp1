import random

from ap1 import *
import pandas as pd
import numpy as np


def ex2a():
    ex5d_text("a.txt")
    ex5d_text("alice29.txt")
    ex5d_text("cp.htm")
    ex5d_image("lena.bmp")
    ex5d_text("Person.java")
    ex5d_text("progc.c")


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

def ex3a(n, m):
    str = ''
    for i in range(n):
        str += random.choice(m)
    return str


alphabet = []
for i in range(26):
    alphabet.append(chr(ord('a')+i))
for i in range(26):
    alphabet.append(chr(ord('A') + i))
for i in range(10):
    alphabet.append(chr(ord('0')+i))
alphabet.append('!')
alphabet.append('?')
alphabet.append('*')
alphabet.append('+')
print(ex3a(100000, alphabet))

list1 = []
for i in range(66):
    list1.append(1)
entropy = -1 * sum(map(lambda x: x / 66 * np.log(x / 66), list1))
print(entropy)