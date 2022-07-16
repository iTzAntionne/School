"""
File:    ab_equality.py
Author:  Antionne Andries
Date:    11/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: Prints out all the permutations of a and b strings given an even length
"""


# Prints out all the permutations of a and b strings given an even length
def ab_equal(n, k, current):
    a_counter = 0
    b_counter = 0

    if n == 0 and k == 0:
        return current

    elif n == 0:
        for i in current:
            if i == "a":
                a_counter += 1
            else:
                b_counter += 1
        if a_counter == b_counter:
            print(current)
    else:
        ab_equal(n - 1, k + 1, current + "a")
        ab_equal(n - 1, k + 1, current + "b")


if __name__ == "__main__":
    ab_equal(6, 0, "")

