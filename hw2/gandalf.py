"""
File:    gandalf.py
Author:  Antionne Andries
Date:    9/17/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It guesses which lord of the rings character you are
"""

race = input("What race is the character? (human/dwarf/elf/maiar/hobbit) ").lower()

if race == "human":
    KingOfG = input("Are you the King of Gondor? ").lower()
    if KingOfG == "yes":
        print("You are the Aragorn the son of Arathorn")
    else:
        ringFrodo = input("Have you tried to take the ring from Frodo? ").lower()
        if ringFrodo == "yes":
            print("You are Boromir")
        else:
            print("You are Theodan")
elif race == "elf":
    matrix = input("Where you in the matrix? ").lower()
    if matrix == "yes":
        print("You are Elrond")
    else:
        print("You are Legolas")
elif race == "maiar":
    goodVsEvil = input("Are you good or evil? ").lower()
    if goodVsEvil == "good":
        print("You are Gandalf")
    else:
        oneRing = input("Did you forge the One Ring? ").lower()
        if oneRing == "yes":
            print("You are Sauron")
        else:
            print("You are Saruman")
elif race == "hobbit":
    one_Ring = input("Do you carry the One Ring? ").lower()
    if one_Ring == "yes":
        print("You are Frodo Baggins")
    else:
        gardener = input("Are you a gardener? ").lower()
        if gardener == "yes":
            print("You are Samwise")
        else:
            print("You are Merry or Pipin")
elif race == "dwarf":
    print("You are Gimli son of Gloin")
else:
    print("You are an  Orc")
