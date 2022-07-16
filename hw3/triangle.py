"""
File:    triangle.py
Author:  Antionne Andries
Date:    9/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: creates a triangle of stars
"""

heightWidth = int(input("What is the height/width of the triangle? "))
for i in range(heightWidth+1):
    print(" " * (heightWidth-i), "*" * i)
