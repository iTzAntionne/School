"""
File:    find_a_plus.py
Author:  Antionne Andries
Date:    10/20/2021
Section: 36
E-mail:  a345@umbc.edu
Description: It outputs true or false depending on if it found a plus shape in a grid with dimensions given by the user
"""
import random


def generate_grid(m, n, seed=0):
   if seed:
      random.seed(seed)
   return [[random.choice(['.', '*']) for _ in range(n)] for _ in range(m)]


def display_grid(the_grid):
   for row in the_grid:
       print(' '.join(row))


def is_plus_there(my_grid):
   plus_found = False

   # Iterates through the 2D array
   for row in range(len(my_grid)):
      for col in range(1, len(my_grid[row])-1):

         # Does a check so I don't get an out of bounds error
         if row == len(my_grid) - 1 and not plus_found:
            return False

         # Find the Plus symbol
         if my_grid[row][col - 1] == "*" and my_grid[row][col] == "*" and my_grid[row][col + 1] == "*":
            if my_grid[row - 1][col] == "*" and my_grid[row + 1][col] == "*":
               plus_found = True
               return plus_found


if __name__ == '__main__':
   numbers = input('Enter the dimensions (and optionally the seed): ').split()
   x = int(numbers[0])
   y = int(numbers[1])
   the_seed = int(numbers[2])
   a_grid = generate_grid(x, y, the_seed)
   display_grid(a_grid)
   print()
   print(is_plus_there(a_grid) is not False)
