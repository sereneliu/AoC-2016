import hashlib

puzzle_input = 'abbhdwsy'

def find_next_char(string):
    password = []
    index = 0
    while len(password) < 8:
        string_index = string + str(index)
        md5_hash = hashlib.md5(string_index.encode('utf-8')).hexdigest()
        if md5_hash.startswith('00000'):
            password.append(md5_hash[5])
        index += 1
    return ''.join(password)

print find_next_char(puzzle_input)