if __name__ == '__main__':
    """
    File:    burger.py
    Author:  Antionne Andries
    Date:    10/1/2021
    Section: 36
    E-mail:  a345@umbc.edu
    Description: Creates a burger with the user choosing what they want
    """
    condiments = []
    burger = []
    cheese = "cheese"
    burgerCounter = 0
    flag = True

    while flag:
        burgerInput = burger.append(input("What do you want to add? "))
        for i in range(len(burger)):
            if burger[0] != "bottom bun":
                print("You must start with the bottom bun!")
                burger.remove(burger[0])
        for i in range(len(burger)):
            if burger[i] == "top bun":
                flag = False
    for element in burger:
        if element not in condiments:
            condiments.append(element)
    condiments.remove('top bun')
    condiments.remove('burger')
    condiments.remove('bottom bun')
    for element in burger:
        if element == "burger":
            burgerCounter += 1
    if cheese in burger:
        condiments.remove('cheese')
        print("You have created a " + str(burgerCounter) + "-cheeseburger with the condiments:")
        if len(condiments) == 0:
            print("No Condiments")
        else:
            print(*condiments, sep=", ")
    else:
        print("You have created a " + str(burgerCounter) + "-hamburger with the condiments: ")
        if len(condiments) == 0:
            print("No Condiments")
        else:
            print(*condiments, sep=", ")
