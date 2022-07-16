"""
File:    which_month_2.py
Author:  Antionne Andries
Date:    9/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: Outputs the future month given the current month and future time skip
"""
months = ["December", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November"]

m = int(input("What month are we starting in (enter as an int)? "))
n = int(input("How many months in the future should we go? "))
futureM = (m+n) % 12

if m > 12:
    print("That is not a month between 1 and 12.")
elif futureM < 13:
    print(months[futureM])
