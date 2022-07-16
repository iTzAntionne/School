"""
File:    people_list.py
Author:  Antionne Andries
Date:    9/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: creates a list of user inputted names and can also give you the longest name
"""
names = []
placeholder = []
removed = []
steps = int(input("How many steps should we run? "))

for i in range(steps):
    command = input("Enter command: ")
    placeholder.extend(command.split())
    if placeholder[0] == "add".lower():
        names.extend(command.split())
        names.remove("add")
        print(placeholder[1], "added.")
        placeholder = []
    elif placeholder[0] == "remove".lower():

        for g in list(names):
            if g == placeholder[1]:
                removed = placeholder[1]
        if len(removed) == 0:
            print("Name not found")
        else:
            names.remove(placeholder[1])
            print(placeholder[1], "removed")
        removed = []
        placeholder = []
    elif placeholder[0] == "max".lower():
        longestName = names[0]
        for k in range(len(names)):
            if longestName < names[k]:
                longestName = names[k]
        print("The max name is", longestName)
        placeholder = []
