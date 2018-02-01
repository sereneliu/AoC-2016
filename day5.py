import hashlib

puzzle_input = 'abbhdwsy'

def find_next_char(string):
    pw_pos = {}
    password = []
    index = 0
    while len(pw_pos) < 8:
        string_index = string + str(index)
        md5_hash = hashlib.md5(string_index.encode('utf-8')).hexdigest()
        if md5_hash.startswith('00000') and md5_hash[5] in '01234567' and md5_hash[5] not in pw_pos.keys():
            pw_pos[md5_hash[5]] = md5_hash[6]
        index += 1
    for i in xrange(8):
        for k, v in pw_pos.items():
            if k == str(i):
                password.append(v)
    return ''.join(password)

print find_next_char(puzzle_input)