import re

with open('day7.txt') as puzzle_file:
    puzzle_input = puzzle_file.read().split('\n')

example_1 = 'abba[mnop]qrst' # supports TLS (abba outside square brackets)
example_2 = 'abcd[bddb]xyyx' # does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets)
example_3 = 'aaaa[qwer]tyui' # does not support TLS (aaaa is invalid; the interior characters must be different)
example_4 = 'ioxxoj[asdfgh]zxcvbn' # supports TLS (oxxo is outside square brackets, even though it's within a larger string)

def contains_ABBA(seq):
    for i in xrange(0, len(seq) - 3):
        if seq[i:i+2] == seq[i+3:i+1:-1] and seq[i] != seq[i+1]:
            return True

def supports_TLS(IP):
    split_IP = re.split('\[|\]', IP)
    hypernet_seq = []
    outside_seq = []
    for seq in split_IP:
        if '[' + seq + ']' in IP:
            hypernet_seq.append(seq)
        else:
            outside_seq.append(seq)
    for h in hypernet_seq:
        if contains_ABBA(h) == True:
                return False
        else:
            for o in outside_seq:
                if contains_ABBA(o) == True:
                    return True

def count_IPs(IP_list):
    IPs = 0
    for IP in IP_list:
        if supports_TLS(IP) == True:
            IPs += 1
    return IPs

print supports_TLS(example_1)
print supports_TLS(example_2)
print supports_TLS(example_3)
print supports_TLS(example_4)

print count_IPs(puzzle_input)