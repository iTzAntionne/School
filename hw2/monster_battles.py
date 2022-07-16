"""
File:    monster_battles.py
Author:  Antionne Andries
Date:    9/17/2021
Section: 36
E-mail:  a345@umbc.edu
Description: it evaluates whether a "monster" is stronger than the other and determines which one would win a battle
"""

m1 = input("What is the name of the first monster? ")
d1 = int(input("How much damage does the first monster do? "))
h1 = int(input("How much hitpoints does the first monster have? "))

m2 = input("What is the name of the second monster? ")
d2 = int(input("How much damage does the second monster do? "))
h2 = int(input("How much hitpoints does the second monster have? "))

if h2/d1 > h1/d2:
    print(m2, "beats", m1)
elif h2/d1 < h1/d2:
    print(m1, "beats", m2)
else:
    print("The two monsters annihilate each other")


