from ap1 import ex4
import pandas as pd
import numpy as np


def ex2a():
    ex4("a.txt")
    ex4("alice29.txt")
    ex4("cp.htm")
    ex4("lena.bmp")
    ex4("Person.java")
    ex4("progc.c")


ex2a()

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
