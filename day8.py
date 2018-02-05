with open('day8.txt') as puzzle_file:
    puzzle_input = [line.split(' ') for line in puzzle_file.read().split('\n')]

def make_screen(width, height):
    screen = []
    for i in range(height):
        screen.append([])
        for _ in range(width):
            screen[i].append('.')
    return screen

def read_instructions(instructions, width, height):
    screen = make_screen(width, height)
    for instruction in instructions:
        if instruction[0] == 'rect':
            x = int(instruction[1][instruction[1].index('x') - 1])
            y = int(instruction[1][instruction[1].index('x') + 1])
            for i in range(y):
                for j in range(x):
                    screen[i][j] = '#'
        elif instruction[0] == 'rotate':
            if instruction[2][0] == 'x':
                x = int(instruction[2][instruction[2].index('=') + 1:])
                y = int(instruction[4])
                new_column = []
                for h in range(height):
                    new_column.append(screen[(h-y) % height][x])
                for i in range(height):
                    screen[i][x] = new_column[i]
            elif instruction[2][0] == 'y':
                y = int(instruction[2][instruction[2].index('=') + 1:])
                x = int(instruction[4])
                new_row = []
                for w in range(width):
                    new_row.append(screen[y][(w-x) % width])
                screen[y] = new_row
    lit = 0
    for row in range(height):
        lit += screen[row].count('#')
    return lit

print read_instructions(puzzle_input, 50, 6)