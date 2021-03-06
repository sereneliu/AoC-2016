with open('day9.txt') as puzzle_file:
    puzzle_input = puzzle_file.read()

def decompressed(file):
    is_decompressed = False
    decompressed_length = 0
    marker = []
    to_be_decomp = []
    skip = 0
    mult = 0
    for i in xrange(len(file)):
        if not is_decompressed:
            if file[i] != '(':
                decompressed_length += 1
            else:
                is_decompressed = True
        elif is_decompressed:
            if skip == 0:
                if file[i] != ')':
                    marker.append(file[i])
                else:
                    marker = ''.join(marker)
                    skip = int(marker[:marker.index('x')]) + 1
                    mult = int(marker[marker.index('x') + 1:])
            elif skip > 1:
                to_be_decomp.append(file[i])
                skip -= 1
            if skip == 1:
                to_be_decomp = ''.join(to_be_decomp)
                decompressed_length += decompressed(to_be_decomp) * mult
                to_be_decomp = []
                marker = []
                is_decompressed = False
                skip -= 1
    return decompressed_length

print decompressed(puzzle_input)