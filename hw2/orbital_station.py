"""
File:    orbital_station.py
Author:  Antionne Andries
Date:    9/17/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It outputs the rotation speed of the station or the station radius.
"""

control = input("Would you like to control 'rotation speed' or 'station radius'? ")
if control == "rotation speed":
    r = int(input("What is the radius of the station? "))
    rpm = ((60 / (2*3.14)) * ((9.8 / r) ** .5))
    print("The rotation speed is", rpm, "rpm")
if control == "station radius":
    speed = int(input("What speed in rpm do you want the station to rotate? "))
    stationRadius = (9.8/((((2*3.14159) * speed)/60)**2))
    print("The station radius is", stationRadius, "meters")


