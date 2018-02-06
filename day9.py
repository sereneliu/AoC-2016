with open('day9.txt') as puzzle_file:
    puzzle_input = puzzle_file.read()

def decompressed(file):
    decompressed = False
    decompressed_length = 0
    marker = []
    skip = 0
    for i in xrange(len(file)):
        if not decompressed:
            if file[i] != '(':
                decompressed_length += 1
            else:
                decompressed = True
        elif decompressed:
            if file[i] != ')' and type(marker) != int:
                marker.append(file[i])
            elif skip == 0:
                marker = ''.join(marker)
                skip = int(marker[:marker.index('x')]) + 1
                marker = (int(marker[:marker.index('x')]) * int(marker[marker.index('x') + 1:]))
            elif skip > 1:
                skip -= 1
            if skip == 1:
                decompressed_length += marker
                marker = []
                decompressed = False
                skip -= 1
    return decompressed_length

print decompressed(puzzle_input)