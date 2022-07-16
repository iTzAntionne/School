"""
File:    minor_key.py
Author:  Antionne Andries
Date:    10/16/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It outputs a musical scale depending on what the user asked for
"""
MUSICAL_NOTES = ["C", "D\u266d", "D", "E\u266d", "E", "F", "G\u266d", "G", "A\u266d", "A", "B\u266d", "B"]
STEPS = [2, 1, 2, 2, 1, 3, 1]


# Turns "C flat" into well..."C*flat symbol*"
def note(user_input):
    check_flats = user_input.split()
    if len(check_flats) >= 2:
        if check_flats[1].lower() == "flat":
            user_input = check_flats[0] + "\u266d"
    return user_input


# Gets the harmonic minor scale for note inputted by user
def scale(starting_note):
    start = note(starting_note)
    index = 0
    scale_list = []
    list_flag = True
    invalid = "There is no starting note " + start

    # Checks if the note is apart of the Harmonic notes list
    if start in MUSICAL_NOTES:

        # finds index of the inputted note
        for i in range(len(MUSICAL_NOTES)):
            if MUSICAL_NOTES[i] == start:
                index = i
        step = index
        i = 0

        # loops through and adds the scale to a list
        while list_flag:
            scale_list.append(MUSICAL_NOTES[step])
            step += STEPS[i]
            i += 1
            if step > 11:
                step -= 12
            if len(scale_list) == 7:
                list_flag = False
        scale_list.append(start)
        return scale_list
    else:
        return invalid


def main():
    flag = True
    print(scale(input("Enter a starting note (D, E flat) ")))
    while flag:
        starting_note = input("Enter a starting note (C, D Flat) ")
        if starting_note.lower() == "quit":
            flag = False
        else:
            print(scale(starting_note))


if __name__ == "__main__":
    main()
