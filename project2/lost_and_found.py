"""
    Starter code for Lost and Found Project 2, CMSC 201 Fall 2021
"""

import json


USE = 'e'
EMPTY = ''
FLOOR = '_'
EXIT = 'x'
DOOR = 'd'
SECRET = 's'
WALL = '*'
ITEMS = 'i'
STARTING_LOCATION = 'start'


def load_map(map_file_name):
    """
        When a map file name is passed the file will load the grid and return it.
        Should you modify this function? No you shouldn't.

    :param map_file_name: a string representing the file name.
    :return: a 2D list which contains the current map.
    """
    with open(map_file_name) as map_file:
        the_map = json.loads(map_file.read())

    return the_map


def get_exit_pos(grid):
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if grid[i][k]["symbol"] == EXIT:
                return [k, i]


def exit_game(grid, move):
    a, b = get_player_pos(grid)
    end_game = False

    if move == "w" and grid[b - 1][a]["symbol"] == EXIT:
        grid[b][a]["symbol"] = FLOOR
        b -= 1
        grid[b][a]["symbol"] = '\u1330'
        print("Good Job on getting to the end ʕ•́ᴥ•̀ʔっ♡")
        end_game = True

    # moves the player down to a valid position
    if move == "s" and grid[b + 1][a]["symbol"] == EXIT:
        grid[b][a]["symbol"] = FLOOR
        b += 1
        grid[b][a]["symbol"] = '\u1330'
        print("Good Job on getting to the end ʕ•́ᴥ•̀ʔっ♡")
        end_game = True

    # moves the player right to a valid position
    if move == "d" and grid[b][a + 1]["symbol"] == EXIT:
        grid[b][a]["symbol"] = FLOOR
        a += 1
        grid[b][a]["symbol"] = '\u1330'
        print("Good Job on getting to the end ʕ•́ᴥ•̀ʔっ♡")
        end_game = True

    # moves the player left to a valid position
    if move == "a" and grid[b][a - 1]["symbol"] == EXIT:
        grid[b][a]["symbol"] = FLOOR
        a -= 1
        grid[b][a]["symbol"] = '\u1330'
        print("Good Job on getting to the end ʕ•́ᴥ•̀ʔっ♡")
        end_game = True

    return end_game


# Unlocks the door for the player if they have the key
def unlock_door(grid, move):
    # updates the player's position
    a, b = get_player_pos(grid)
    key_to_find = "requires"

    if move == "w" and grid[b - 1][a]["symbol"] == DOOR:
        if key_to_find not in grid:
            grid[b - 1][a]["symbol"] = FLOOR

        if grid[b - 1][a]["requires"] in inventory:
            check_e = input("Press 'e' to unlock door:")
            if check_e == "e":
                grid[b - 1][a]["symbol"] = FLOOR
        else:
            print("Stop joshing, go get key please.")

    # moves the player down to a valid position
    if move == "s" and grid[b + 1][a]["symbol"] == DOOR:
        if key_to_find not in grid:
            grid[b - 1][a]["symbol"] = FLOOR

        if grid[b + 1][a]["requires"] in inventory:
            check_e = input("Press 'e' to unlock door:")
            if check_e == "e":
                grid[b + 1][a]["symbol"] = FLOOR
        else:
            print("Stop joshing, go get key please.")


    # moves the player right to a valid position
    if move == "d" and grid[b][a + 1]["symbol"] == DOOR:
        if key_to_find not in grid:
            grid[b - 1][a]["symbol"] = FLOOR

        if grid[b][a + 1]["requires"] in inventory:
            check_e = input("Press 'e' to unlock door:")
            if check_e == "e":
                grid[b][a + 1]["symbol"] = FLOOR
        else:
            print("Stop joshing, go get key please.")

    # moves the player left to a valid position
    if move == "a" and grid[b][a - 1]["symbol"] == DOOR:
        if key_to_find not in grid:
            grid[b - 1][a]["symbol"] = FLOOR

        if grid[b][a - 1]["requires"] in inventory:
            check_e = input("Press 'e' to unlock door:")
            if check_e == "e":
                grid[b][a - 1]["symbol"] = FLOOR
        else:
            print("Stop joshing, go get key please.")

    return [b, a]


# Finds the players position
def get_player_pos(grid):
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if grid[i][k]["symbol"] == '\u1330':
                return [k, i]


# Moves the player around
def move_valid_pos(grid, move):
    valuables = []

    for rows in range(len(grid)):
        for col in range(len(grid[rows])):
            for items in grid[rows][col]["items"]:
                valuables.append(items)

    # updates the player's position
    a, b = get_player_pos(grid)

    # moves the player up to a valid position and checks if there is an item on that spot
    if move == "w" and grid[b - 1][a]["symbol"] == FLOOR:
        if grid[b - 1][a]["items"] != valuables:
            grid[b][a]["symbol"] = FLOOR
            b -= 1
            grid[b][a]["symbol"] = '\u1330'
        else:
            grid[b][a]["symbol"] = FLOOR
            b -= 1
            inventory.append(grid[b][a]["items"])
            grid[b][a]["items"] = valuables
            grid[b][a]["symbol"] = '\u1330'

    # moves the player down to a valid position and checks if there is an item on that spot
    if move == "s" and grid[b + 1][a]["symbol"] == FLOOR:
        if grid[b + 1][a]["items"] != valuables:
            grid[b][a]["symbol"] = FLOOR
            b += 1
            grid[b][a]["symbol"] = '\u1330'
        else:
            grid[b][a]["symbol"] = FLOOR
            b += 1
            inventory.append(grid[b][a]["items"])
            grid[b][a]["items"] = EMPTY
            grid[b][a]["symbol"] = '\u1330'

    # moves the player right to a valid position and checks if there is an item on that spot
    if move == "d" and grid[b][a + 1]["symbol"] == FLOOR:
        if grid[b][a + 1]["items"] != valuables:
            grid[b][a]["symbol"] = FLOOR
            a += 1
            grid[b][a]["symbol"] = '\u1330'
        else:
            grid[b][a]["symbol"] = FLOOR
            a += 1
            inventory.append(grid[b][a]["items"])
            grid[b][a]["items"] = EMPTY
            grid[b][a]["symbol"] = '\u1330'

    # moves the player left to a valid position and checks if there is an item on that spot
    if move == "a" and grid[b][a - 1]["symbol"] == FLOOR:
        if grid[b][a - 1]["items"] != valuables:
            grid[b][a]["symbol"] = FLOOR
            a -= 1
            grid[b][a]["symbol"] = '\u1330'
        else:

            grid[b][a]["symbol"] = FLOOR
            a -= 1
            inventory.append(grid[b][a]["items"])
            grid[b][a]["items"] = EMPTY
            grid[b][a]["symbol"] = '\u1330'

    return [b, a]


def get_player_starting_pos(grid):
    key_to_find = "start"

    # Finds the starting position of the player if there is one
    if key_to_find in grid:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]["start"]:
                    grid[row][col]["symbol"] = '\u1330'
                    return [grid[row], grid[row][col]]

    # Sets the player position to 0,0 if no start pos is found
    else:
        grid[0][0]["symbol"] = '\u1330'
        return [0, 0]


# prints out the grid
def lost_and_found(grid):

    for rows in grid:
        for place in rows:
            if place["items"]:
                print(ITEMS, end=" ")
            else:

                # turns 's' into an asterisk
                if place["symbol"] == SECRET:
                    place["symbol"] = WALL

                # prints out the symbols onto the board
                print(place["symbol"], end=" ")
        print()


if __name__ == '__main__':
    map_file_name = input('What map do you want to load? ')
    the_game_map = load_map(map_file_name)
    playing_game = True
    inventory = []
    attempts = 0

    get_player_starting_pos(the_game_map)

    # Loads the game map
    if the_game_map:
        lost_and_found(the_game_map)

    while playing_game:

        movement_input = input("Enter (w,a,s,d) to move:  | Enter 'q' to quit: ")

        # Quits the game
        if movement_input == "q":
            playing_game = False

        # Checks if the player wants to move then moves them
        elif movement_input == "w" or movement_input == "a" or movement_input == "s" or movement_input == "d":
            unlock_door(the_game_map, movement_input)
            move_valid_pos(the_game_map, movement_input.strip())
            lost_and_found(the_game_map)

            if exit_game(the_game_map, movement_input):
                playing_game = False

        # Tells you to enter a valid input
        else:
            if attempts == 0:
                print("Invalid input")
                print()
                attempts += 1
            elif attempts == 1:
                print("Hey man I think you should pick a valid choice...")
                print()
                attempts += 1
            elif attempts == 2:
                print("Third time's the charm?")
                print()
                attempts += 1
            elif attempts == 3:
                print("Bruv... D I R E C T I O N S are right there...")
                print()
                attempts += 1
            elif attempts == 4:
                print("-.-")
                print()
                attempts += 1
            elif attempts == 5:
                print("This is why NationWide is not on your side")
                print()
                attempts += 1
            elif attempts == 6:
                print("Did you know that o number from 1 to 999 includes the letter 'a' in its word form")
                print()
                attempts += 1
            else:
                print("You're done! You're done!")
                print()
