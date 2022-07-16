"""
File:    how_deep.py
Author:  Antionne Andries
Date:    11/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: Recursively finds the deepest list
"""


# Recursively finds the deepest list
def how_deep(list_struct):
    depth = []
    final = 0
    for sublist in list_struct:
        depth.append(how_deep(sublist))
    for i in depth:
        if i > final:
            final = i
    return final + 1


if __name__ == '__main__':
    print(how_deep([[[], [], [], [[[]]]], []]))
    print(how_deep([]))
    print(how_deep([[], []]))
    print(how_deep([[[]], [], [[]], [[[]]]]))
    print(how_deep([[[[], [[]], [[[]]], [[[[]]]]]]]))
    print(how_deep([[[], []], [], [[], []]]))
