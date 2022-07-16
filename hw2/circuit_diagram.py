"""
File:    circuit_diagram.py
Author:  Antionne Andries
Date:    9/17/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It models a circuit with and, or and not gates
"""
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
e = int(input("Enter e: "))

q = 0
w = 0

if a == 1 and (not d == 1):
    print("The circuit outputs 1")
elif b == 1 and c == 1:
    q = b
    if e == 1 or q:
        w = 1
        if a == 1 and w == 1:
            print("The circuit outputs 1")
else:
    print("The circuit outputs 0")
"""
if a == 0 and (not d == 0):
    print("The circuit outputs 0")
"""
