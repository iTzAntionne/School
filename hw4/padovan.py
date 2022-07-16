if __name__ == '__main__':
    """
    File:    padovan.py
    Author:  Antionne Andries
    Date:    10/1/2021
    Section: 36
    E-mail:  a345@umbc.edu
    Description: it tells you how many steps it takes to get to or exceed a user inputted goal
    """
    padovanList = [1, 1, 1]
    goal = int(input("Enter the goal to reach in the Padovan sequence: "))
    count = 0
    flag = True
    n = 3
    i = 2

    while flag:
        p = padovanList[n-2] + padovanList[n-3]
        padovanList.append(p)
        n += 1
        i += 1
        if padovanList[i] >= goal:
            for k in range(len(padovanList)):
                count += 1
            flag = False
    if goal == 1:
        print("It takes", goal, "step to get there or above")
    else:
        print("It takes", count, "steps to get there or above")
