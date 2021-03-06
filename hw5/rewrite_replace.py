"""
File:    rewrite_replace.py
Author:  Antionne Andries
Date:    10/16/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It replaces a part of a given string with another string provided by the user.
"""


# replaces the instant of the slice with the replacement string
def rewrite_replace(full_string, slices, replacement):
    if slices in full_string:
        new_word = replacement.join(full_string.split(slices))
        return "This is your new word " + new_word
    else:
        return "No instances of the string you were looking for were found, this is your string " + full_string


def main():
    total_string = input("What is the total string? ")
    find_string = input("What string should we look for? ")
    replace_string = input("What should we replace that string with? ")
    print(rewrite_replace(total_string, find_string, replace_string))


if __name__ == "__main__":
    main()
