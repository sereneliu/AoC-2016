with open('day2.txt') as puzzle_file:
    puzzle_input = puzzle_file.read().split('\n')

example_input = [
    'ULL', 
    'RRDDD',
    'LURDL',
    'UUUUD']

keypad = ['123', '456', '789']

def up(x, y):
    return x, y - 1

def down(x, y):
    return x, y + 1

def right(x, y):
    return x + 1, y

def left(x, y):
    return x - 1, y

directions = {
    'U': up,
    'D': down,
    'R': right,
    'L': left
}

def bathroom_code(some_input):
    (x, y) = (1, 1)
    code = []
    for line in some_input:
        for i in xrange(len(line)):
            direction = line[i]
            if (direction == 'U' and y > 0) or (direction == 'D' and y < 2) or (direction == 'R' and x < 2) or (direction == 'L' and x > 0):
                (x, y) = directions[direction](x, y)
            else:
                (x, y) = (x, y)
            if i == len(line) - 1:
                code.append(keypad[y][x])
    return ''.join(code)

# print bathroom_code(example_input) # expect: 1985
print bathroom_code(puzzle_input)