with open('day1.txt') as puzzle_file:
    puzzle_input = puzzle_file.read().split(', ')
    
r = dict(zip('nesw', 'eswn'))
l = dict(zip('nesw', 'wnes'))

test1 = ['R2', 'L3'] # expect: 5
test2 = ['R2', 'R2', 'R2'] # expect: 2
test3 = ['R5', 'L5', 'R5', 'R3'] # expect: 12

def blocks_away(coordinates, direct_facing, directions):
    facing = direct_facing
    (x, y) = coordinates
    for direction in directions:
        if direction[0] == 'R':
            facing = r[facing]
        else:
            facing = l[facing]
        blocks = int(direction[1:])
        if facing == 'n':
            y += blocks
        elif facing == 's':
            y -= blocks
        elif facing == 'e':
            x += blocks
        else:
            x -= blocks
    return (x, y, abs(x) + abs(y))

print blocks_away((0, 0), 'n', test1)
print blocks_away((0, 0), 'n', test2)
print blocks_away((0, 0), 'n', test3)
print blocks_away((0, 0), 'n', puzzle_input)