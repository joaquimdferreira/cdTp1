import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def ex5a(n, u, r):
    print('ex1')
    curr = u
    for i in range(n):
        print(curr)
        curr *= r


# ex5a(10, 1, 2)


def ex5b(a, b):
    if a == b:
        print('mdc is: %d' % a)
    elif a == 0:
        print('mdc is: %d' % b)
    elif b == a:
        print('mdc is: %d' % a)
    elif a > b:
        ex5b(a - b, b)
    else:
        ex5b(a, b - a)


# print('------------------------------------------------------------------------------------')
# print('ex2')
# ex5b(105, 252)


def ex5c(file_name):
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


def ex5d_text(file_name):
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
    entropy = -1 * sum(map(lambda x: x / total_chars * np.log(x / total_chars), chars.values()))
    print('Entropy is: %f' % entropy)
    df = pd.DataFrame(data=list(zip(chars.keys(), chars.values(), char_prob)),
                      columns=['Char', 'n of Occurrences', 'Inf Propria'])
    print(df.to_string())
    plt.bar(range(len(chars.keys())), chars.values())
    plt.title("Histogram of file " + file_name)
    plt.ylabel("No. of Occ")
    plt.xticks(range(len(chars.keys())), chars.keys())
    plt.show()
    entropy = -1 * sum(map(lambda x: x / total_chars * np.log(x / total_chars), chars.values()))
    print('Entropy is: %f' % entropy)


# make work for color images with py lib
def ex5d_image(image_name):
    print('------------------------------------------------------------------------------------')
    print('ex4')
    pixels = {}
    f = open(image_name, "r", encoding='iso-8859-1')
    while 1:
        c = ord(f.read(1))
        if not c:
            break
        elif c in pixels.keys():
            pixels[c] += 1
        else:
            pixels[c] = 1
    pixels = dict(sorted(pixels.items(), key=lambda x: x[0]))
    total_pixels = sum(pixels.values(), 0)
    pixel_prob = map(lambda x: x / total_pixels, pixels.values())
    entropy = -1 * sum(map(lambda x: x / total_pixels * np.log(x / total_pixels), pixels.values()))
    print('Entropy is: %f' % entropy)
    df2 = pd.DataFrame(data=list(zip(pixels.keys(), pixels.values(), pixel_prob)),
                       columns=['Pixel', 'n of Occurrences', 'Inf Propria'])
    print(df2.to_string())
    plt.bar(range(len(pixels.keys())), pixels.values())
    plt.title("Histogram of file " + image_name)
    plt.ylabel("No. of Occ")
    plt.xticks(range(len(pixels.keys())), pixels.keys())
    plt.show()
    entropy2 = -1 * sum(map(lambda x: x / total_pixels * np.log(x / total_pixels), pixels.values()))
    print('Entropy is: %f' % entropy2)

# ex5d("alice29.txt")
