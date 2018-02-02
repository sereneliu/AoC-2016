import re

with open('day7.txt') as puzzle_file:
    puzzle_input = puzzle_file.read().split('\n')

example_1 = 'abba[mnop]qrst' # supports TLS (abba outside square brackets)
example_2 = 'abcd[bddb]xyyx' # does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets)
example_3 = 'aaaa[qwer]tyui' # does not support TLS (aaaa is invalid; the interior characters must be different)
example_4 = 'ioxxoj[asdfgh]zxcvbn' # supports TLS (oxxo is outside square brackets, even though it's within a larger string)

def is_ABBA(seq):
    if seq[0:2] == seq[:1:-1]  and seq[0] != seq[1]:
        return True

def supports_TLS(IP):
    split_IP = re.split('\[|\]', IP)
    for seq in split_IP:
        for i in xrange(0, len(seq) - 3):
            if is_ABBA(seq[i:i+4]) == True:
                if '[' + seq + ']' in IP:
                    return False
                else:
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