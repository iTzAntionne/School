"""
File:    find_a_plus.py
Author:  Antionne Andries
Date:    10/20/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It moves you to a coordinate designated by the user
"""
import random

ALLOWED = '_'
FORBIDDEN = '*'


def walk_around(the_grid, walk_command):
    x = 0
    y = 0
    for direction in walk_command:
        if direction == "u" and the_grid[y - 1][x] == ALLOWED:
            y -= 1
        if direction == "d" and y + 1 < len(the_grid) and the_grid[y + 1][x] == ALLOWED:
            y += 1
        if direction == "r" and x + 1 < len(the_grid) and the_grid[y][x + 1] == ALLOWED:
            x += 1
        if direction == "l" and the_grid[y][x - 1] == ALLOWED:
            x -= 1
    return [y, x]


def generate_map(m, n, the_seed=0):
    if the_seed:
        random.seed(the_seed)
    the_map = [[random.choice([ALLOWED, FORBIDDEN]) for _ in range(n)] for _ in range(m)]
    the_map[0][0] = ALLOWED
    return the_map


def display_map(the_map):
    for i in range(len(the_map)):
        print(' '.join(the_map[i]))


if __name__ == '__main__':
    # clearly this next line of code is forbidden in general.
    the_map = generate_map(*list(map(int, input('Enter m n (optionally: seed): ').split())))
    display_map(the_map)
    move_command = input('What is the move command? ')
    print(walk_around(the_map, move_command))

