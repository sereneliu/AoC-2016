with open('day2.txt') as puzzle_file:
    puzzle_input = puzzle_file.read().split('\n')

example_input = [
    'ULL', 
    'RRDDD',
    'LURDL',
    'UUUUD']

keypad = ['123', '456', '789']

actual_keypad = ['  1  ',  ' 234 ', '56789', ' ABC ', '  D  ']

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

def bathroom_code(some_input, some_keypad, start):
    (x, y) = start
    code = []
    for line in some_input:
        for i in xrange(len(line)):
            direction = line[i]
            if (direction == 'U' and y > 0) or (direction == 'D' and y < (len(some_keypad) - 1)) or (direction == 'R' and x < (len(some_keypad) - 1)) or (direction == 'L' and x > 0):
                (a, b) = directions[direction](x, y)
                if some_keypad[b][a] != ' ':
                    (x, y) = (a, b)
            if i == len(line) - 1:
                code.append(some_keypad[y][x])
    return ''.join(code)

# print bathroom_code(example_input, keypad, (1, 1)) # expect: 1985
# print bathroom_code(puzzle_input, keypad, (1, 1))
# print bathroom_code(example_input, actual_keypad, (0, 2)) # expect: 5DB3
print bathroom_code(puzzle_input, actual_keypad, (0, 2))