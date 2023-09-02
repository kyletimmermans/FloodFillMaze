#!/usr/bin/env python3

'''
Kyle Timmermans
FloodFillMaze v2.0
Sept 2, 2023
Python 3.11.4

Note: maze[i][j] is a char-value held in a position-index and
      i (row) and j (column) are the position indexes
'''

import sys
import random
from colorama import Fore, init


'''
Random Maze Generation

Maze: Must be a square, e.g. 14x14

Path: Must be inside perimeter, start at left side,
can't touch itself (like snake game),
cannot be diagonal, can only touch one other opening

How it works: The outer-most while loop is just
waiting to check if we've reached the end of the maze
(from left to right). The inner-while loop checks that
each move of the path is placed correctly. Thus,
the goal of both is to get the path all the way across
with each piece of the path being correctly placed.
'''
def generate_maze(size):
    # All individual lists, not one big sub-list
    maze = [['#'] * size for _ in range(size)]

    # Choose left-most starting point (in perimeter)
    random_start = random.randint(1, size-2)
    # On start point, cant go up or down bc we are on the perimeter
    # Also cant go left because its -1, so always have to be +1 in (right over 1)
    maze[random_start][0], maze[random_start][1] = ' ', ' '

    # Start y at 1 bc of above comments, we dont want to be on perimeter
    x, y = find_start(maze), 1
    end = False
    while end is False:  # While not at end (right-most column)

        valid_move = False
        # To restart if the path gets stuck
        # and prevent an infinite loop
        block_counter = 0
   
        while valid_move is False: # For each path space, check if it's valid
            temp_x, temp_y = x, y  # Reset back to norm each loop
            random_move = random.choice(['up', 'down', 'left', 'right'])

            if random_move == "up":
                temp_x -= 1
            elif random_move == "down":
                temp_x += 1
            elif random_move == "left":
                temp_y -= 1
            elif random_move == "right":
                temp_y += 1
                # If we reached the right most wall, no need to check,
                # it's the final move, just place it
                if temp_y == size-1:
                    end = True
                    maze[temp_x][temp_y] = ' '
                    return maze

            # Conditions List

            # If not in perimeter
            if temp_x == 0 or temp_x == (size-1) or temp_y == 0 or temp_y == (size-1):
                valid_move = False
                continue

            # If already taken
            if maze[temp_x][temp_y] == ' ':
                valid_move = False
                continue

            # All chars touching the current space (up, down, left, right)
            degrees_of_space = [maze[temp_x-1][temp_y],
                                maze[temp_x+1][temp_y],
                                maze[temp_x][temp_y-1],
                                maze[temp_x][temp_y+1]]

            # +1 if move goes to a "#"
            wall_count = len([symbol for symbol in degrees_of_space if symbol == '#'])

            # If touching other parts of maze path incorrectly (it needs 3 '#')
            if wall_count != 3:
                block_counter += 1
                # If we're blocked in and going in circles, reset
                if block_counter >= 100:
                    maze = [['#'] * size for _ in range(size)]
                    maze[random_start][0], maze[random_start][1] = ' ', ' '
                    x, y = find_start(maze), 1
                valid_move = False
                continue
            # If all conditions passed, its a valid move
            else:
                # Since its a good move, we can stick it in the coords tracker
                x, y = temp_x, temp_y
                maze[x][y] = ' '
                valid_move = True
                block_counter = 0


# Find start of maze
def find_start(maze):
    for i in range(len(maze)):
        if maze[i][0] == ' ':  # Y is 0, always starting from left most point of 2D array
            return i


# Traverse maze left to right
def traverse_maze(maze):
    x, y = find_start(maze), 0  # Y is always 0 because the maze will always begin at the first column
    end = False
    while end is False:  # While not at end
        # 4 Directions: X=Rows, Y=Columns
        up = maze[x-1][y]
        down = maze[x+1][y]
        left = maze[x][y-1]
        right = maze[x][y+1]
        if y == len(maze)-2 and right == ' ':  # Reached farthest right
            maze[x][y], maze[x][y+1] = u'\u265b', u'\u265b'  # Now set the last ones to solved as well b/c they won't be reached
            end = True  # End while loop, maze completely solved
        elif up == ' ':  # Keep going if up is a space
            maze[x][y] = u'\u265b'
            x -= 1
        elif down == ' ':  # Keep going if down is a space
            maze[x][y] = u'\u265b'
            x += 1
        elif left == ' ':  # Keep going if left is a space
            maze[x][y] = u'\u265b'
            y -= 1
        elif right == ' ':  # Keep going if right is a space
            maze[x][y] = u'\u265b'
            y += 1
    return maze


def print_maze(maze):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    # random.sample() will always return 2 distinct colors (maze & piece visibility)
    maze_color, piece_color = random.sample(colors, 2)
    print('\n')  # Newline for formatting
    for row in range(len(maze)):  # For every line in maze
        for elem in range(len(maze[row])):  # For every element in line
            if maze[row][elem] == '#':
                print(f"{maze_color}{maze[row][elem]}", end=' ')
            else:
                print(f"{piece_color}{maze[row][elem]}", end=' ')
        print('\n', end='')  # Keep new lines close together


# Driver
if __name__ == '__main__':

    if '--version' in sys.argv or '-v' in sys.argv:
        print("\nFloodFillMaze v2.0\n")
        quit()

    init() # Colorama init

    maze = generate_maze(14) # Generate 14x14 maze
    completed_maze = traverse_maze(maze) # Solve maze
    print_maze(completed_maze) # Print maze
