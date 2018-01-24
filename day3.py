import re

with open('day3.txt') as puzzle_file:
    puzzle_input = [tuple(map(int, re.match(' +(\d+) +(\d+) +(\d+)', puzzle_line).groups())) for puzzle_line in puzzle_file.read().splitlines()]

def find_valid_triangles(some_input):
    valid_triangles = 0
    for (a, b, c) in some_input:
        if a + b > c and b + c > a and a + c > b:
            valid_triangles += 1
    return valid_triangles

print find_valid_triangles(puzzle_input)

def find_vertical_triangles(some_input):
    valid_triangles = 0
    for j in xrange(3):
        for i in xrange(0, len(some_input), 3):
            a = some_input[i][j]
            b = some_input[i+1][j]
            c = some_input[i+2][j]
            if a + b > c and b + c > a and a + c > b:
                valid_triangles += 1
    return valid_triangles

print find_vertical_triangles(puzzle_input)