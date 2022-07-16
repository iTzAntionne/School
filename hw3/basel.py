"""
File:    basel.py
Author:  Antionne Andries
Date:    9/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: calculates the basel problem up to a certain user input
"""

n = int(input("What is the number of terms you want to sum? "))
total = 1
answer = 0
for i in range(n):
    answer += 1/(total**2)
    total += 1
print("The approximation for the", n, "terms is", answer)
