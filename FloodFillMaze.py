#!/usr/bin/env python3

'''
Kyle Timmermans
FloodFillMaze v1.0
Feb 25th, 2020

Future updates: Random maze gen, Determine array size from input,
Start and end point = anywhere on perimeter, More Input sanitation, trail able to
go through itself

Note: maze[i][j] is a value held in a position-index, i and j are the position indexes
'''

# Colored text module
import colorama
from colorama import Fore
colorama.init()

# Create maze board
# 12 x 12 test
# Must be a square, e.g. 5x5, 7x7
# Can't touch itself, like snake game
test_maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
             ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
             ['#', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' '],
             ['#', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#'],
             [' ', ' ', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#'],
             ['#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', '#', '#'],
             ['#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#'],
             ['#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#'],
             ['#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#'],
             ['#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', '#'],
             ['#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
             ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]


# Find start of maze
def find_start(maze):
    for i in range(len(maze)):
        if maze[i][0] == ' ':  # Y is 0, always starting from left most point of 2D array
            return i


# Traverse maze left to right
def traverse(maze):
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


# Print the maze as green, print the runner as red
def print_maze(maze):
    print('\n')  # Newline for formatting
    for row in range(len(maze)):  # For every line in maze
        for elem in range(len(maze[row])):  # For every element in line
            if maze[row][elem] == '#':
                print(Fore.GREEN + maze[row][elem], end=' ')  # Keep elements close and make maze green
            else:
                print(Fore.RED + maze[row][elem], end=' ') # Keep elements close and make the runner red
        print('\n', end='')  # Keep new lines close together


# Driver
print_maze(traverse(test_maze))  # Print the returned traversed maze
