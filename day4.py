with open('day4.txt') as puzzle_file:
    puzzle_input = puzzle_file.read().split('\n')

def is_real(room):
    encrypted_name = {}
    for character in room[:room.index('[')]:
        if character.isalpha():
            if character in encrypted_name:
                encrypted_name[character] += 1
            else:
                encrypted_name[character] = 1
    checksum = []
    sorted_values = sorted(encrypted_name.values(), reverse=True)
    for n in sorted_values:
        same_values = []
        for k, v in encrypted_name.items():
            if v == n:
                same_values.append(k)
        for same_value in sorted(same_values):
            if same_value not in checksum:
                checksum.append(same_value)
    if ''.join(checksum[:5]) == room[room.index('[') + 1:room.index(']')]:
        return True
    else:
        return False

def sector_ID_sum(some_input):
    all_sector_IDs = []
    for room in some_input:
        if is_real(room) == True:
            sector_ID = []
            for character in room[:room.index('[')]:
                if character.isdigit():
                    sector_ID.append(character)
            ID = int(''.join(sector_ID))
            all_sector_IDs.append(ID)
            encrypted = room[:room.index(str(ID)) - 1]
            real_name = []
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            shift = ID % 26
            for letter in encrypted:
                if letter == '-':
                    real_name.append(' ')
                else:
                    real_name.append(alphabet[(alphabet.index(letter) + shift) % 26])
            if ''.join(real_name) == 'northpole object storage':
                return ID
#    return sum(all_sector_IDs)

print sector_ID_sum(puzzle_input)