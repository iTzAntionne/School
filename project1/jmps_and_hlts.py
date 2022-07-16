"""
File:    jmps_and_hlts.py
Author:  Antionne Andries
Date:    10/31/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It mimics a gave of chutes and ladders with modified rules
"""

import random

GRID_WIDTH = 8
GRID_HEIGHT = 3
DICE_SIDES = 6


# Simulates a game of chutes and ladders until the player hits hlt
def play_game(game_map):
    game_ongoing = True
    position = 0
    score = 0
    roll = 0
    length = int(grid_size_seed[0])
    display_grid()

    # Loops through the game until you hit hlt
    while game_ongoing:
        if game_map[position][0:3] != "jmp":
            roll = roll_dice()
            position = position_finder(position, length, roll)
        else:
            position = jmp(position)

        print("Pos:", position, "Score:", score, "Instruction:", game_map[position], "Rolled:",
              roll)

        score = math(position, score)

        # Ends the game
        if game_map[position] == "hlt":
            game_ongoing = False
            print("Final Pos:", position, "Final Score:", score, "Instruction:", game_map[position])


def position_finder(position, size, roll):
    """
        Finds the position of the player on the board
    """
    position = (int(position) + roll) % size
    return position


def display_grid():
    """
        Displays the grid
    """
    for i in range(int(grid_size_seed[0])):
        fill_grid_square(grid, int(grid_size_seed[0]), i, str(i) + "\n" + random_commands[i])

    for i in range(len(grid)):
        print(''.join(grid[i]))


def jmp(position):
    """"
        :param position - The position on the board
        function jumps to a specified space
    """
    if random_commands[position][0:3] == "jmp":
        position = (random_commands[position][4:len(random_commands[position])])

    return int(position)


def math(position, score):
    """"
        :param position - The position on the board
        function keeps track of the score
    """

    if random_commands[position][0:3] == "add":
        score += int(random_commands[position][4:len(random_commands[position])])

    if random_commands[position][0:3] == "sub":
        score -= int(random_commands[position][4:len(random_commands[position])])

    if random_commands[position][0:3] == "mul":
        score *= int(random_commands[position][4:len(random_commands[position])])

    return score


def generate_random_map(length, the_seed=0):
    """
        :param length - the length of the map
        :param the_seed - the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    """
    if the_seed:
        random.seed(the_seed)
    map_list = []
    for _ in range(length - 2):
        random_points = random.randint(1, 100)
        random_position = random.randint(0, length - 1)
        map_list.append(random.choices(['nop', f'add {random_points}', f'sub {random_points}', f'mul {random_points}', f'jmp {random_position}', 'hlt'], weights=[5, 2, 2, 2, 3, 1], k=1)[0])

    return ['nop'] + map_list + ['hlt']


def make_grid(table_size):
    """
        :param table_size: this needs to be the length of the map
        :return: returns a display grid that you can then modify with fill_grid_square (it's a 2d-grid of characters)
    """
    floating_square_root = table_size ** (1 / 2)

    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_height = int_square_root
    if int_square_root * (int_square_root - 1) >= table_size:
        table_height -= 1

    the_display_grid = [[' ' if j % GRID_WIDTH else '*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        if i % GRID_HEIGHT else ['*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        for i in range(table_height * GRID_HEIGHT + 1)]
    return the_display_grid


def fill_grid_square(display_grid, size, index, message):
    """
    :param display_grid:  the grid that was made from make_grid
    :param size:  this needs to be the length of the total map, otherwise you may not be able to place things correctly.
    :param index: the index of the position where you want to display the message
    :param message: the message to display in the square at position index, separated by line returns.
    """
    floating_square_root = size ** (1 / 2)
    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_row = index // int_square_root
    table_col = index % int_square_root

    if table_row % 2 == 0:
        column_start = GRID_WIDTH * table_col
    else:
        column_start = GRID_WIDTH * (int_square_root - table_col - 1)

    for r, message_line in enumerate(message.split('\n')):
        for k, c in enumerate(message_line):
            display_grid[GRID_HEIGHT * table_row + 1 + r][column_start + 1 + k] = c


def roll_dice():
    """
        Call this function once per turn.

        :return: returns the dice roll
    """
    return random.randint(1, DICE_SIDES)


if __name__ == '__main__':
    flag = True
    while flag:
        # Gets the length of the game and seed
        grid_size_seed = input("Enter size and seed: ").split()
        grid = make_grid(int(grid_size_seed[0]))
        random_commands = generate_random_map(int(grid_size_seed[0]), int(grid_size_seed[1]))

        play_game(random_commands)

        # Asks if they want to play again
        play = input("Do you want to play again? (y/n): ").lower()
        if play == "n" or play == "no":
            flag = False
