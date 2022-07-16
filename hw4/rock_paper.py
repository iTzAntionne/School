if __name__ == '__main__':
    """
    File:    rock_paper.py
    Author:  Antionne Andries
    Date:    10/1/2021
    Section: 36
    E-mail:  a345@umbc.edu
    Description: You play rock paper scissors vs a copmuter
    """
    import random
    flag = True

    while flag:
        compChoice = random.choice(["rock", "paper", "scissors"])
        user = input("Enter rock, paper, or scissors to play, stop to end. ")
        if user == compChoice:
            print("Both " + user + ", there is a tie.")
        elif user == "rock":
            if compChoice == "paper":
                print("Paper covers rock, you lose")
            else:
                print("Rock crushes scissors, you win.")
        elif user == "paper":
            if compChoice == "rock":
                print("Paper covers rock, you win.")
            else:
                print("Scissors cut paper, you lose.")
        elif user == "scissors":
            if compChoice == "rock":
                print("Rock crushes scissors, you lose.")
            else:
                print("Scissors cut paper, you win.")
        elif user == "stop":
            flag = False
        else:
            print("You need to select rock, paper or scissors.")
