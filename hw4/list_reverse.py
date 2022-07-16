if __name__ == '__main__':
    """
    File:    list_reverse.py
    Author:  Antionne Andries
    Date:    10/1/2021
    Section: 36
    E-mail:  a345@umbc.edu
    Description: it reverses a list of strings
    """
    reversedList = []
    nums = []
    nonNums = []
    inputtedList = input("Enter a list separated by commas: ")
    string = ""
    digits = "48, 49, 50, 51, 52, 53, 54, 55, 56, 57"
    findOrd = 0
    placeholder = inputtedList.split(",")
    lengthHold = placeholder
    for i in lengthHold:
        string += i
        for k in range(len(string)):
            findOrd = ord(string[k])
        if str(findOrd) in digits:
            nums.append(i)
        else:
            nonNums.append(i)
    for i in range(len(nonNums)-1, -1, -1):
        reversedList.append(nonNums[i])
    if len(nonNums) == 0:
        print("The new list was empty")
    else:
        print(*reversedList, sep=", ")
