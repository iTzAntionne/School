"""
File:    which_month.py
Author:  Antionne Andries
Date:    9/17/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It prints out the future month given a time frame to skip
"""
m = int(input("What month are we starting in (enter as a number)? "))
n = int(input("How many months in the future should we go? "))

k = ((m + n) % 12)

if m <= 12:
    if k == 1:
        print("The month will be January")
    if k == 2:
        print("The month will be February")
    if k == 3:
        print("The month will be March")
    if k == 4:
        print("The month will be April")
    if k == 5:
        print("The month will be May")
    if k == 6:
        print("The month will be June")
    if k == 7:
        print("The month will be July")
    if k == 8:
        print("The month will be August")
    if k == 9:
        print("The month will be September")
    if k == 10:
        print("The month will be October")
    if k == 11:
        print("The month will be November")
    if k == 0:
        print("The month will be December")
else:
    print("That is not a month between 1 and 12.")
