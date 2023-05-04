import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def ex1(n, u, r):
    print('ex1')
    curr = u
    for i in range(n):
        print(curr)
        curr *= r


# ex5a(10, 1, 2)


def ap1ex5b(a, b):
    if a == b:
        print('mdc is: %d' % a)
    elif a == 0:
        print('mdc is: %d' % b)
    elif b == a:
        print('mdc is: %d' % a)
    elif a > b:
        ap1ex5b(a - b, b)
    else:
        ap1ex5b(a, b - a)


# print('------------------------------------------------------------------------------------')
# print('ex2')
# ex5b(105, 252)


def ap1ex5c(file_name):
    print('------------------------------------------------------------------------------------')
    print('ex3')
    chars = {}
    f = open(file_name, "r")
    while 1:
        c = f.read(1)
        if not c:
            break
        if c in chars.keys():
            chars[c] += 1
        else:
            chars[c] = 1
    chars = dict(sorted(chars.items(), key=lambda x: x[0]))
    min_char = min(chars.items(), key=lambda x: x[1])
    max_char = max(chars.items(), key=lambda x: x[1])
    print('min is: ' + min_char[0] + ' - %d' % min_char[1])
    print('max is: ' + max_char[0] + ' - %d' % max_char[1])


# ex5c("a.txt")


def ap1ex5d(file_name):
    print('------------------------------------------------------------------------------------')
    print('ex4')
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
    char_prob = map(lambda x: x / total_chars, chars.values())
    entropy = -1 * sum(map(lambda x: x / total_chars * np.log2(x / total_chars), chars.values()))
    print('Entropy is: %f' % entropy)
    df = pd.DataFrame(data=list(zip(chars.keys(), chars.values(), char_prob)),
                      columns=['Char', 'n of Occurrences', 'Inf Propria'])
    print(df.to_string())
    plt.bar(range(len(chars.keys())), chars.values())
    plt.title("Histogram of file " + file_name)
    plt.ylabel("No. of Occ")
    plt.xticks(range(len(chars.keys())), chars.keys())
    plt.show()
    entropy = -1 * sum(map(lambda x: x / total_chars * np.log2(x / total_chars), chars.values()))
    print('Entropy is: %f' % entropy)


# ap1ex5d("alice29.txt")
