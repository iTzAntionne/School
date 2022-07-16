"""
File:    lottery.py
Author:  Antionne Andries
Date:    10/16/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It checks if your lottery ticket matches the winning one and give you moeny in respect to how many nums match
"""


# checks if the tickets matches the winning one and outputs the money won according to user's ticket
def check_ticket(test_ticket, winning_ticket, grand_prize):
    invalid = "These numbers are not valid"
    check_user_ticket_nums = False
    check_winning_ticket_nums = False
    track = 0
    check_powerball = False
    temphold1 = test_ticket.split()
    temphold2 = winning_ticket.split()

    powerball_money_won = [4, 4, 7, 100, 50000, grand_prize]
    non_powerball_money_won = [0, 0, 0, 7, 100, 1000000]

    # separates the ticket numbers away from the power ball number
    user_ticket = [temphold1[0:5], temphold1[-1]]
    winning_one = [temphold2[0:5], temphold2[-1]]
    power_ball = winning_one[-1]

    # checks if the numbers in the user's ticket are valid
    for i in range(len(user_ticket[0])):
        if int(user_ticket[0][i]) > 69 or int(user_ticket[0][i]) < 1:
            check_user_ticket_nums = True

    # checks if the winning ticket numbers are valid
    for i in range(len(winning_one[0])):
        if int(winning_one[0][i]) > 69 or int(winning_one[0][i]) < 1:
            check_winning_ticket_nums = True

    # checks if the user inputted valid numbers
    if (int(power_ball) > 27 or int(power_ball) < 1) or check_user_ticket_nums or check_winning_ticket_nums or (int(user_ticket[1]) > 27 or int(user_ticket[1]) < 1):
        return invalid
    else:

        # checks if the winning power ball and user power ball are the same
        if user_ticket[-1] == power_ball:
            check_powerball = True

        # checks if the first 5 nums match
        for i in winning_one[0]:
            if i in user_ticket[0]:
                track += 1

        # calculates how much money you won, after checking how many balls were correctly guessed
        if check_powerball:
            return "This ticket wins $" + str(powerball_money_won[track])
        else:
            return "This ticket wins $" + str(non_powerball_money_won[track])


def main():
    winning_ticket = input("What is the winning ticket? (Put the powerball last) ").strip()
    test_ticket = input("What is the test ticket? (Put the powerball last) ").strip()
    grand_prize = int(input("What is the grand prize? ").strip())
    print(check_ticket(test_ticket, winning_ticket, grand_prize))


if __name__ == "__main__":
    main()
