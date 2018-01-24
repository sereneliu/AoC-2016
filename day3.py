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