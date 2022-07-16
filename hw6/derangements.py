"""
File:    derangements.py
Author:  Antionne Andries
Date:    11/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: returns the derangements of something
"""


# Finds all the derangements of any given string of n digits long
def derangement(num):
    if num == 0:
        return 1
    else:
        derangements = num * derangement(num - 1) + ((-1)**num)

    return derangements


if __name__ == '__main__':
    for i in range(20):
        print(i, derangement(i))
