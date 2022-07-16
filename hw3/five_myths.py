"""
File:    five_myths.py
Author:  Antionne Andries
Date:    9/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: outputs the true "myth" stories and false ones separately
"""

truth = []
false = []
placeholder = []
subject = input("Tell the subject: ")

for i in range(5):
    myths = placeholder.append(input("Tell me a myth about " + subject + ": "))

for i in range(5):
    TrueFalse = input("Is it actually a myth: " + placeholder[i] + "? (no,yes) ")
    if TrueFalse == "no":
        false.append(placeholder[i])
    else:
        truth.append(placeholder[i])

print("Here are the myths: ", truth)
print("Here are the non-myths which shouldn't have been included: ", false)

