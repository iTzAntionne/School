"""
File:    ab_verify.py
Author:  Antionne Andries
Date:    11/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: Verifies whether there are more a's or equal to b's given that the a's appeared before the b's
"""


# Verifies whether there are more a's or equal to b's given that the a's appeared before the b's
def ab_verify(string, counter):
    a_counter = 0

    if string[counter] == "a":
        a_counter += 1
        return ab_verify(string, counter + 1)

    if counter >= len(string)//2:
        return True
    else:
        return False


if __name__ == "__main__":
    s = input('Enter a string to test: ')
    while s != 'quit':
        print(ab_verify(s, 0))
        s = input('Enter a string to test: ')
